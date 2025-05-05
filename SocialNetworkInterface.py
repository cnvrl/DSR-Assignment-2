from abc import ABC, abstractmethod
from Node import Node

class SocialNetworkInterface(ABC):
    """
    An abstract base class to represent accounts and their relationships as a graph.

    This interface includes methods for processing data, suggesting friends, reminding birthday events,
    and finding mutual friends.

    @version Dec 2024
    """

    @abstractmethod
    def process_file(self) -> None:
        """
        Reads data from a file (e.g., data.txt) and creates nodes and edges among them.

        This method should handle parsing the file and populating the graph structure.
        """
        pass

    @abstractmethod
    def suggest_friends(self, current_person: Node) -> list[Node]:
        """
        Suggest friends for a given account. Suggestions should include friends of friends
        who live in the same suburb.

        :param current_person: The current account for which to suggest friends.
        :return: A list of no more than 5 suggested friends (Node objects).
        """
        pass

    @abstractmethod
    def remind_bd_events(self, current_person: Node) -> str:
        """
        Returns all friends of a given account, sorted based on their birthday, along with
        a string representing the time until their next birthday.

        :param current_person: The current account for which to remind birthday events.
        :return: A string representation of friends sorted by their birthday, including
                 the time until their birthday.
        """
        pass

    @abstractmethod
    def get_mutual_friends(self, x: Node, y: Node) -> str:
        """
        Finds mutual friends between two accounts.

        :param x: The first account (Node object).
        :param y: The second account (Node object).
        :return: A string containing the names of all mutual friends, separated by ",".
        """
        pass