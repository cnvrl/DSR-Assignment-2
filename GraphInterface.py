from abc import ABC, abstractmethod
from datetime import date
from typing import Set, Optional
from Node import Node
from Edge import Edge

class GraphInterface(ABC):
    """
    A Python abstract base class that defines methods for an undirected graph (nodes + edges). with methods for adding/removing nodes and edges,
    retrieving neighbors, and representing the graph as a string.

    @version Dec 2024
    """

    @abstractmethod
    def add_node(self, node_id: int, name: str, dob: date, suburb: str) -> Node:
        """
        Create and add a new vertex to the graph with the given attributes.

        :param node_id: The unique ID of the node.
        :param name: The name associated with the node.
        :param dob: The date of birth of the node.
        :param suburb: The suburb associated with the node.
        :return: The added Node object.
        """
        pass

    @abstractmethod
    def add_edge(self, from_node: Node, to_node: Node) -> None:
        """
        Add a new edge to the graph between two nodes.

        :param from_node: The starting node of the edge.
        :param to_node: The ending node of the edge.
        """
        pass

    @abstractmethod
    def remove_edge(self, from_node: Node, to_node: Node) -> None:
        """
        Remove an edge between two nodes in the graph.

        :param from_node: The source node of the edge.
        :param to_node: The destination node of the edge.
        """
        pass

    @abstractmethod
    def remove_node(self, node: Node) -> None:
        """
        Remove a node from the graph.

        :param node: The node to be removed.
        """
        pass

    @abstractmethod
    def get_neighbors(self, node: Node) -> Optional[Set[Edge]]:
        """
        Return a set of edges representing all neighbors of the given node.

        :param node: The node whose neighbors are to be retrieved.
        :return: A set of edges to neighboring nodes, or None if there are no neighbors.
        """
        pass

    @abstractmethod
    def __str__(self) -> str:
        """
        Display the graph and its vertices in the format:
        person 1 --> friend1    friend2 ...
        person 2 --> friend1    friend2 ...

        :return: A string representation of the graph.
        """
        pass