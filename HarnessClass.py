import datetime
from Node import Node
from Node import Edge
from Graph import Graph
from SocialNetwork import SocialNetwork


class HarnessClass():
    """
    A test harness for all tasks in Assignment 3, 2019 (graph, hashing, 
    reading data from files, PriorityQueue, etc.)
    
    Author: Zhongju Wang
    Version: Dec 2024
    """

    n = None
    n2 = None
    n3 = None
    n4 = None

    @staticmethod
    def main():
        """
        Main function to run all tests for the assignment.
        """
        # Testing Task 1
        print(" ------*****------ Task 1 begins ------*****------")
        print(" ---- Testing Node and Edge classes begins ----")
        HarnessClass.test_task1()
        print(" ------*****------ Task 1 ends ------*****------\n\n")

        # Testing Task 2
        print(" ------*****------ Task 2 begins ------*****------")
        print(" ---- Testing hashing ----")
        HarnessClass.test_task2()
        print(" ------*****------ Task 2 ends ------*****------\n\n")

        # Testing Task 3
        print(" ------*****------ Task 3 begins ------*****------")
        print(" ---- Testing graph ----")
        HarnessClass.test_task3()
        print(" ------*****------ Task 3 ends ------*****------\n\n")
        
        # Testing Task 4-6
        print(" ------*****------ Task 4-6 begins ------*****------")
        HarnessClass.test_social_network()
        print(" ------*****------ Task 4-6 ends ------*****------\n\n")

        print("Other things to consider:\n"
              "- testing\n"
              "- naming conventions\n"
              "- python docstrings\n"
              "- documentation\n")
        
    @staticmethod
    def test_task1():
        """
        Testing Task 1: basic operations in the Node and Edge classes.
        """
        try:
            HarnessClass.n = Node(1, "B", datetime.date(2018, 10, 30), "Bonner")
            HarnessClass.n2 = Node(2, "B", datetime.date(2018, 9, 30), "Ford")
            print(f"{HarnessClass.n.name}, {HarnessClass.n.dob}, {HarnessClass.n.suburb}\t")
        except Exception as e:
            print(e)

        try:
            edge = Edge(HarnessClass.n2)
            print(f"Actual: {edge.friend.suburb}\t", end="")
            if edge.friend.suburb == "Ford":
                print("Status: Edge test --> PASS")
        except Exception as e:
            print(f"Actual: {e} - Status: Edge test --> FAIL")

    @staticmethod
    def test_task2():
        """
        Testing Task 2: hashing and equality.
        """
        print(HarnessClass.n2.__hash__())
        print(HarnessClass.n2 == HarnessClass.n)

    @staticmethod
    def test_task3():
        """
        Testing Task 3: the Graph class.
        """
        g = Graph()

        # Add nodes to the graph
        try:
            v0 = g.add_node(0, "V0", datetime.date(2010, 10, 30), "A")
            v1 = g.add_node(1, "V1", datetime.date(2010, 10, 30), "B")
            print("Number of nodes:", len(g.node_list))     #expected output: 2
        except Exception as e:
            print("Add node error:", e)

        # Add and remove edges
        try:
            g.add_edge(v0, v1)
            print("Added edge V0 <--> V1")      #expected output
        except Exception as e:
            print("Add edge error:", e)

        try:
            g.remove_edge(v0, v1)
            print("Removed edge V0 <--> V1")    #expected output
        except Exception as e:
            print("Remove edge error:", e)

        # Test adding and removing nodes
        try:
            g.remove_node(v1)
            print("Removed node V1")        #expected output
        except Exception as e:
            print("Remove node error:", e)

        try:
            v1 = g.add_node(1, "V1", datetime.date(2010, 10, 30), "B")
            print("Re-added node V1")       #expected output
        except Exception as e:
            print("Re-add node error:", e)

        # Test retrieving neighbors
        try:
            g.add_edge(v0, v1)
            neighbors = g.get_neighbors(v1)
            print("Neighbors of V1:", [n.get_name() for n in neighbors])        #expected output: ["V0"]
        except Exception as e:
            print("Get neighbors error:", e)

        # Test string representation of the graph
        try:
            print("Graph representation:\n" + str(g))     #expected output: V0: --> V1 & V1: --> V0
        except Exception as e:
            print("Graph representation error:", e)

        # Test removing a node with edges
        try:
            v2 = g.add_node(2, "V2", datetime.date(2010, 10, 30), "C")
            g.add_edge(v1, v2)
            print("Added node V2 and edge V1 <--> V2")
            g.remove_node(v1)
            print("Removed node V1 with edge to V2")      #expected output
            print(g)
        except Exception as e:
            print("Remove node with edges error:", e)

        # Test removing a non-existent node
        try:
            g.remove_node(v1)
            print("Removed non-existent node V1")
        except Exception as e:
            print("Remove non-existent node error:", e)     #expected output

        # Test adding an edge with a non-existent node
        try:
            g.add_edge(v0, v1)
            print("Added edge V0 <--> V1 with non-existent node")
        except Exception as e:
            print("Add edge with non-existent node error:", e)      #expected output

        # Test adding an edge that already exists
        try:
            g.add_edge(v0, v1)
            print("Added edge V0 <--> V1 that already exists")
        except Exception as e:
            print("Add edge that already exists error:", e)     #expected output

        # Test removing an edge that doesn't exist
        try:
            g.remove_edge(v0, v1)
            print("Removed edge V0 <--> V1 that doesn't exist")
        except Exception as e:
            print("Remove edge that doesn't exist error:", e)       #expected output

        # Test adding a node that already exists
        try:
            v0 = g.add_node(0, "V0", datetime.date(2010, 10, 30), "A")
            print("Added node V0 that already exists")
        except Exception as e:
            print("Add node that already exists error:", e)         #expected output    

        # Test adding a node with the same ID but different attributes
        try:
            v1 = g.add_node(1, "V1", datetime.date(2010, 10, 30), "C")
            print("Added node V1, replacing previous attributes")       #expected output
        except Exception as e:
            print("Add node with same ID but different attributes error:", e)

        # Test adding an edge with a non-existent node
        try:
            g.add_edge(v0, v3)
            print("Added edge V0 <--> V3 with non-existent node")
        except Exception as e:
            print("Add edge with non-existent node error:", e)      #expected output

        
    @staticmethod
    def test_social_network():
        """
        Testing Task 4-6: SocialNetwork functionality.
        """
        try:
            driver = SocialNetwork()
            print(driver.sn)
            neighbors = driver.sn.get_neighbors(driver.sn.node_list[1])
        except Exception as e:
            print(e)

        # Test suggest_friends
        try:
            friends_of_friends = driver.suggest_friends(driver.sn.node_list[1])
        except Exception as e:
            print(e)

        # Test get_mutual_friends
        try:
            mutual_friends = driver.get_mutual_friends(
                driver.sn.node_list[1], driver.sn.node_list[4]
            )
        except Exception as e:
            print(e)

        # Test remind_bd_events
        try:
            print(f"Actual: {driver.remind_bd_events(driver.sn.node_list[1])}\t") #which person youre reminding
        except Exception as e:
            print(e)

# Run the main function
if __name__ == "__main__":
    HarnessClass.main()