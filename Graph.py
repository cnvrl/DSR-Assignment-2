
from datetime import datetime, date
from typing import Set, Optional
from Node import Node, Edge
from GraphInterface import GraphInterface
import re
from typing import Dict, Set


class Graph:
    """
    A class that represents a graph using an adjacency list.
    Each node in the graph is represented by an instance of the Node class, and edges are represented by instances
    of the Edge class.
    """
    def __init__(self):
        """
        Initializes an empty graph with an empty dictionary to hold nodes.
        """
        self.node_list: Dict[int, Node] = {}

    def add_node(self, node_id: int, name: str, dob: date, suburb: str) -> Node:
        """
        Adds a new node to the graph.
        :param node_id: The ID of the new node.
        :param name: The name of the new node.
        :param dob: The date of birth of the new node.
        :param suburb: The suburb of the new node.
        :return: The newly created node.
        """
        if node_id in self.node_list:
            raise Exception(f"Node with ID {node_id} already exists.")
        new_node = Node(node_id, name, dob, suburb)
        self.node_list[node_id] = new_node                                                          # Store the node in the graph
        return new_node

    def add_edge(self, from_node: Node, to_node: Node) -> None:
        """
        Adds an edge between two nodes in the graph.
        :param from_node: The starting node of the edge.
        :param to_node: The ending node of the edge.
        :return: None
        """
        if from_node.get_id() not in self.node_list or to_node.get_id() not in self.node_list:      # Check if both nodes exist in the graph
            raise Exception("One or both nodes not found in the graph.")

        if to_node.get_id() not in from_node.adj:                                                   # Adds the edge to both nodes 
            from_node.adj[to_node.get_id()] = Edge(to_node)
            to_node.adj[from_node.get_id()] = Edge(from_node)

        else:
            raise Exception("Edge already exists between nodes.")

    def remove_edge(self, from_node: Node, to_node: Node) -> None:
        """
        Removes an edge between two nodes in the graph.
        :param from_node: The starting node of the edge.
        :param to_node: The ending node of the edge.
        :return: None
        """
        
        if from_node.get_id() not in self.node_list or to_node.get_id() not in self.node_list:      # Check if both nodes exist in the graph
            raise Exception("One or both nodes not found in the graph.")
       
        if to_node.get_id() not in from_node.adj or from_node.get_id() not in to_node.adj:          # Check if the edge exists   
            raise Exception("Edge does not exist between the specified nodes.")

        from_node.adj.pop(to_node.get_id())
        to_node.adj.pop(from_node.get_id())

    def remove_node(self, node: Node) -> None:
        """
        Removes a node from the graph and all edges associated with it.
        :param node: The node to be removed.
        :raises Exception: If the node is not found in the graph.
        :return: None
        """
        node_id = node.get_id()
        if node_id not in self.node_list:
            raise Exception("Node not found in graph.")

        for other in self.node_list.values():                                                       # Remove this node from other nodes' adjacency lists
            other.adj.pop(node_id, None)

        del self.node_list[node_id]                                                                 # Remove the node from the graph    

    def get_neighbors(self, node: Node) -> Set[Node]:
        """
        Returns a set of neighbors (adjacent nodes) for the given node.
        :param node: The node for which to find neighbors.
        :return: A set of nodes that are neighbors of the given node
        """
        if node.get_id() not in self.node_list:
            raise Exception("Node not found in graph.")
        return {edge.friend for edge in node.adj.values()}                                          # Get the set of friends from the adjacency list

    def __str__(self) -> str:
        """
        Returns a string representation of the graph, showing each node and its friends.
        :param node: The node for which to find neighbors.
        :return: A string representation of the graph.
        """
        result = []
        for node in sorted(self.node_list.values(), key=lambda n: n.get_id()):                      # Sort nodes by ID   
            friends = [edge.friend.get_name() for edge in node.adj.values()]                        
            line = f"{node.get_name()}: <--> {'    '.join(friends)}"
            result.append(line)                                                                     # Add the node and its friends to the result list    
        return "\n".join(result)
