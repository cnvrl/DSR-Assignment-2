from NodeInterface import NodeInterface
from datetime import date
from typing import Dict

class Node(NodeInterface):
    """
    Represents a vertex in the graph with its adjacency list of edges.

    @version Dec 2024
    @autho Zhongju Wang
    """

    def __init__(self, id: int, name: str, dateOB: date, suburb: str):
        """
        Construct a new vertex in the graph with the supplied name, dob, and suburb.

        :param id: ID of the node
        :param name: Name of the node
        :param dob: Date of birth of the node
        :param suburb: Suburb of the node
        """
        self.id = id
        self.name = name
        self.dateOB = dateOB
        self.suburb = suburb
        self.adj: Dict[int, 'Edge'] = {}

    def get_id(self) -> int:
        return self.id

    def get_name(self) -> str:
        return self.name
    
    def get_date_ob(self) -> date:
        return self.dateOB
    
    def get_suburb(self) -> str:
        return self.suburb

    def __str__(self) -> str:
        return f'ID: {self.id}, Name: {self.name}, Suburb: {self.suburb}, DOB: {self.dob}'

    def __hash__(self) -> int:
        hash_val = 0
        prime = 31

        for i, c in enumerate(self.name.lower()):
            hash_val += (i + 1) * ord(c) * prime

        hash_val += self.dateOB.year * 17

        hash_val += self.id * 13

        return hash_val

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Node):
            return NotImplemented
        return (self.id == other.id and self.name == other.name and self.dateOB == other.dob and self.suburb == other.suburb)

    def __lt__(self, other: object) -> bool:
        if not isinstance(other, Node):
            return NotImplemented
        return self.id < other.id

class Edge:
    def __init__(self, friend: Node):
        self.friend = friend

    def __str__(self):
        return f"friend= {{{self.friend.id}, {self.friend.name}, {self.friend.dateOB}, {self.friend.suburb}}}"


def main() -> None:
    n1 = Node(1, "Minna Whittaker", date(1980, 6, 15), "Majura")
    n2 = Node(2, "Gillian Garnett", date(1994, 11, 27), "Majura")
    n3 = Node(3, "Stephen Ernest", date(2026, 11, 1), "Canberra")
    e1 = Edge(n2)
    n1.adj[n2.id] = e1

    print(n1)
    print(n2)
    print(n3)
    print(e1)

    node_set = {n1, n2, n3}
    print(len(node_set))  # Should be 3 if hash/eq work
 

# Main function to create and test the Node class
if __name__ == "__main__":
    main()