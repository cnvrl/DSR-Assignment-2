from NodeInterface import NodeInterface
from datetime import date
from typing import Dict

class Node(NodeInterface):
    """
    Represents a vertex in the graph with its adjacency list of edges.

    @version Dec 2024
    @autho Zhongju Wang
    """

    def __init__(self, id: int, name: str, dob: date, suburb: str):
        """
        Construct a new vertex in the graph with the supplied name, dob, and suburb.

        :param id: ID of the node
        :param name: Name of the node
        :param dob: Date of birth of the node
        :param suburb: Suburb of the node
        """
        self.id = id
        self.name = name
        self.dob = dob
        self.suburb = suburb
        self.adj: Dict[int, 'Edge'] = {}

    def get_id(self) -> int:
        """
        Get the ID of the node.

        :return: ID of the node
        """
        return self.id

    def get_name(self) -> str:
        """
        Get the name of the node.
        
        :return: Name of the node
        """
        return self.name
    
    def get_date_ob(self) -> date:
        """
        Get the date of birth of the node.

        :return: Date of birth of the node
        """
        return self.dob
    
    def get_suburb(self) -> str:
        """
        Get the suburb of the node.
        
        :return: Suburb of the node
        """
        return self.suburb

    def __str__(self) -> str:
        """
        Get a string representation of the node.
        
        :return: String representation of the node
        """
        return f'ID: {self.id}, Name: {self.name}, Suburb: {self.suburb}, DOB:{self.dob}'

    def __hash__(self) -> int:
        """
        Compute a hash value for the node based on its attributes.
        
        :return: Hash value of the node
        """
        hash_val = 0
        prime = 31

        for i, c in enumerate(self.name.lower()):
            hash_val += (i + 1) * ord(c) * prime

        hash_val += self.dob.year * 17

        hash_val += self.id * 13

        return hash_val

    def __eq__(self, other: object) -> bool:
        """
        Check if two nodes are equal based on their attributes.
        
        :param other: The other node to compare with
        :return: True if the nodes are equal and False if not 
        :rtype: bool 
        :raise TypeError: If the other object is not a Node
        """
        if not isinstance(other, Node):
            return NotImplemented
        return (self.id == other.id and self.name == other.name and self.dob == other.dob and self.suburb == other.suburb)

    def __lt__(self, other: object) -> bool:
        """
        Compare two nodes based on their IDs.
        
        :param other: The other node to compare with
        :return: True if this node's ID is less than the other node's ID
        :rtype: bool
        :raise TypeError: If the other object is not a Node "NotImplemented"
        """
        if not isinstance(other, Node):
            return NotImplemented
        return self.id < other.id

class Edge:
    """
    Represents an edge in the graph, which connects two nodes.

    """
    def __init__(self, friend: Node):
        """
        Construct a new edge with the supplied friend node.
        
        :param friend: The friend node connected by this edge
        """
        self.id = friend.id
        self.friend = friend

    def __str__(self):
        """
        Get a string representation of the edge.
        :return: String representation of the edge
        """
        return f"friend= {{{self.friend.id}, {self.friend.name}, {self.friend.dob}, {self.friend.suburb}}}"


def main() -> None:
    """
    Main function to test the Node and Edge classes.
    """
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
    """
    Run the main function to test the Node and Edge classes.
    """
    main()