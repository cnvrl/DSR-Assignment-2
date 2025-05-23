import datetime
from queue import PriorityQueue
from Node import Node, Edge 
from Graph import Graph
from SocialNetworkInterface import SocialNetworkInterface
import os


class SocialNetwork(SocialNetworkInterface):
    """
    Represents accounts and their relationships as a graph.
    Implements the SocialNetworkInterface to provide functionality for:
    - Reading and processing data from files
    - Suggesting friends
    - Finding mutual friends
    - Reminding birthday events
    """

    def __init__(self):
        """
        Initializes the social network by creating an empty graph and processing the data file.
        """
        self.sn = Graph()
        self.process_file()

    def process_file(self) -> None:
        """
        Reads data from a file and populates the graph with nodes and edges.
        """
        path = os.path.join(os.path.dirname(__file__), 'data.txt')
        all_data = []

        # First pass: add nodes
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                parts = line.strip().split('\t')
                if len(parts) != 3:
                    continue
                id_str, name, rest = parts
                id = int(id_str)
                items = [x.strip() for x in rest.split(',')]
                dob = datetime.datetime.strptime(items[0], "%Y-%m-%d").date()
                suburb = items[1]
                friends = list(map(int, items[2:]))
                self.sn.add_node(id, name, dob, suburb)
                all_data.append((id, friends))

        # Second pass: add edges
        for id, friends in all_data:
            node = self.sn.node_list.get(id)
            for friend_id in friends:
                friend_node = self.sn.node_list.get(friend_id)
                try:
                    self.sn.add_edge(node, friend_node)
                except Exception:
                    continue  # skip if edge already exists

    def suggest_friends(self, current_person: Node) -> list[Node]:
        """
        Suggests friends for the current person based on their friends' friends.
        :param current_person: The person for whom to suggest friends.
        :return: A list of suggested friends.
        """
        suggestions = set()
        current_neighbors = self.sn.get_neighbors(current_person)
        for friend in current_neighbors:
            friends_of_friend = self.sn.get_neighbors(friend)
            for candidate in friends_of_friend:
                if (
                    candidate.get_id() != current_person.get_id()
                    and candidate not in current_neighbors
                    and candidate.get_suburb() == current_person.get_suburb()
                ):
                    suggestions.add(candidate)
        return sorted(list(suggestions), key=lambda n: n.get_id())[:5]

    def get_mutual_friends(self, x: Node, y: Node) -> str:
        """
        Finds mutual friends between two nodes.
        :param x: The first node.
        :param y: The second node.
        :return: A string of mutual friends' names.
        """
        neighbors_x = self.sn.get_neighbors(x)
        neighbors_y = self.sn.get_neighbors(y)
        mutual = neighbors_x.intersection(neighbors_y)
        return ", ".join(sorted([n.get_name() for n in mutual]))

    def remind_bd_events(self, current_person: Node) -> str:
        """
        Reminds the current person of upcoming birthdays of their friends.
        :param current_person: The person for whom to remind birthdays.
        :return: A string of upcoming birthdays.
        """
        today = datetime.date.today()
        pq = PriorityQueue()

        def birthday_delta(friend):
            """
            Calculate the number of days until the next birthday of a friend.
            :param friend: The friend whose birthday is to be calculated.
            :return: A timedelta object representing the difference in days.
            """
            dob = friend.get_date_ob()
            next_birthday = dob.replace(year=today.year)
            if next_birthday < today:
                next_birthday = next_birthday.replace(year=today.year + 1)
            delta = next_birthday - today
            return delta

        for friend in self.sn.get_neighbors(current_person):
            delta = birthday_delta(friend)
            pq.put((delta.days, friend))

        result = [f"Hey {current_person.get_name()}:->"]
        while not pq.empty():
            days, friend = pq.get()
            dob = friend.get_date_ob()
            next_birthday = dob.replace(year=today.year)
            if next_birthday < today:
                next_birthday = next_birthday.replace(year=today.year + 1)
            delta = next_birthday - today

            years = delta.days // 365
            months = (delta.days % 365) // 30
            days_left = (delta.days % 365) % 30

            result.append(f"{friend.get_name()} has their birthday after {years} Year, {months} Months, {days_left} days")

        return "\n".join(result)
