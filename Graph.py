
from datetime import date
from Node import Node
from Edge import Edge
from GraphInterface import GraphInterface


"""
constructs an undirected graph with some basic operations: addNode,
removeNode, addEdge, getNeighbors, etc.

@author Zhongju Wang
@version Dec 2024
@see Edge
@see Node
"""

class Graph(GraphInterface):
    """
    Constructs an undirected graph with basic operations like addNode, removeNode, addEdge, getNeighbors, etc.
    """

    def __init__(self):
        """
        Initialize an empty graph that holds all nodes (people) in this graph
        """
        self.node_list: dict[int, Node] = {}

# Main function to create and test the Graph class
if __name__ == "__main__":
    # Create a new graph
    g = Graph()
