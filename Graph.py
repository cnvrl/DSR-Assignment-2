from datetime import datetime, date
from typing import Set, Optional
from Node import Node
from Node import Edge
from GraphInterface import GraphInterface
import re
from typing import Dict, Set


class Graph:
    def __init__(self):
        self.node_list: Dict[int, Node] = {}

    def add_node(self, node_id: int, name: str, dob: date, suburb: str) -> Node:
        if node_id in self.node_list:
            raise Exception(f"Node with ID {node_id} already exists.")
        new_node = Node(node_id, name, dob, suburb)
        self.node_list[node_id] = new_node
        return new_node

    def add_edge(self, from_node: Node, to_node: Node) -> None:
        if from_node.get_id() not in self.node_list or to_node.get_id() not in self.node_list:
            raise Exception("One or both nodes not found in the graph.")

        if to_node.get_id() not in from_node.adj:
            from_node.adj[to_node.get_id()] = Edge(to_node)
            to_node.adj[from_node.get_id()] = Edge(from_node)
        else:
            raise Exception("Edge already exists between nodes.")

    def remove_edge(self, from_node: Node, to_node: Node) -> None:
        from_node.adj.pop(to_node.get_id(), None)
        to_node.adj.pop(from_node.get_id(), None)

    def remove_node(self, node: Node) -> None:
        node_id = node.get_id()
        if node_id not in self.node_list:
            raise Exception("Node not found in graph.")

        # Remove this node from other nodes' adjacency lists
        for other in self.node_list.values():
            other.adj.pop(node_id, None)

        # Remove the node itself
        del self.node_list[node_id]

    def get_neighbors(self, node: Node) -> Set[Node]:
        if node.get_id() not in self.node_list:
            raise Exception("Node not found in graph.")
        return {edge.friend for edge in node.adj.values()}

    def __str__(self) -> str:
        result = []
        for node in sorted(self.node_list.values(), key=lambda n: n.get_id()):
            friends = [edge.friend.get_name() for edge in node.adj.values()]
            line = f"{node.get_name()}: --> {' '.join(friends)}"
            result.append(line)
        return "\n".join(result)
    

if __name__ == "__main__":

    g = Graph()
    n1 = g.add_node(1, "Minna Whittaker", date(1980, 6, 15), "Majura")
    n2 = g.add_node(2, "Gillian Garnett", date(1994, 11, 27), "Majura")
    n3 = g.add_node(3, "Stephen Ernest", date(2026, 11, 1), "Canberra")

    g.add_edge(n1, n2)
    g.add_edge(n2, n3)

    print(g)

    # Output:
    # Minna Whittaker: --> Gillian Garnett
    # Gillian Garnett: --> Minna Whittaker Stephen Ernest
    # Stephen Ernest: --> Gillian Garnett

