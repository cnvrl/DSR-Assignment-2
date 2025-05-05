import datetime
from queue import PriorityQueue
from Node import Node
from Edge import Edge
from Graph import Graph
from Post import Post
from SocialNetworkInterface import SocialNetworkInterface
import os
import re



"""
represents accounts and their relationship as a graph

@author Zhongju Wang
@version Dec 2024
"""


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
        Constructs a SocialNetwork object by reading data files twice.
        - The first read adds all nodes.
        - The second read creates connections (edges) between nodes.
        """
        self.sn = Graph()  # Initialize the graph
        pass

# Main function to create and test the SocialNetwork class
if __name__ == "__main__":
    driver = SocialNetwork()
    # Print the graph structure
    print(driver.sn)

    pass