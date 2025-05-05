from NodeInterface import NodeInterface
from datetime import date, timedelta, datetime
from queue import PriorityQueue


class Node(NodeInterface):
    """
    Represents a vertex in the graph with its adjacency list of edges.

    @version Dec 2024
    @author Zhongju Wang
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
    
    def get_id(self) -> int:
        return self.id
    
    def get_name(self) -> str:
        return self.name
    
    def get_suburb(self) -> str:
        return self.suburb
    
    def get_date_ob(self) -> date:
        return self.dob
    
    def __str__(self) -> str:
        return print(f'ID: {self.id}, Name: {self.name}, Suburb: {self.suburb}, DOB: {self.dob}')

    def __hash__(self) -> int:
        pass

    def __eq__(self, other: object) -> bool:
        pass

    def __lt__(self, other: object) -> bool:
        pass

def main(self) -> None:
        pass 


# Main function to create and test the Node class
if __name__ == "__main__":
    pass