import networkx as nx
import matplotlib.pyplot as plt

#create object of graph
my_Graph = nx.Graph()

#add nodes/points on a graph
#jubili line
my_Graph.add_node('A') #stratford
my_Graph.add_node('B') #westhum [value = 20]
my_Graph.add_node('C') #canning town
my_Graph.add_node('D') #canary warf [value = 50]

#add lines to connect nodes on a graph
my_Graph.add_edge('A', 'B')
my_Graph.add_edge('B', 'C')
my_Graph.add_edge('C', 'D')

#aset attributes to jubili line
nx.set_node_attributes(my_Graph, {'A': 10, 'B': 20, 'C': 30, 'D': 50}, name='A1')

#add nodes/points on a graph
#city line
my_Graph.add_node('E') #Illford
my_Graph.add_node('F') #Barking
my_Graph.add_node('G') #Eastham
my_Graph.add_node('H') #Plaisto
my_Graph.add_node('I') #Westhum [value = 20]

#add lines to connect nodes on a graph
my_Graph.add_edge('E', 'F')
my_Graph.add_edge('F', 'G')
my_Graph.add_edge('G', 'H')
my_Graph.add_edge('H', 'I')

nx.set_node_attributes(my_Graph, {'E': 100, 'F': 90, 'G': 70, 'H': 60, 'I': 20}, name='B1')

#add nodes/points on a graph
#DLR line
my_Graph.add_node('J') #Bow Charch
my_Graph.add_node('K') #Polar
my_Graph.add_node('L') #West india Quay
my_Graph.add_node('M') #canary Warf [value = 50]

#add lines to connect nodes on a graph
my_Graph.add_edge('J', 'K')
my_Graph.add_edge('K', 'L')
my_Graph.add_edge('L', 'M')

nx.set_node_attributes(my_Graph, {'J': 85, 'K': 75, 'L': 65, 'M': 50}, name='C1')

print(my_Graph.number_of_nodes())

#get node dictionary
A1_Node_Dictionary = nx.get_node_attributes(my_Graph, 'A1')
B1_Node_Dictionary = nx.get_node_attributes(my_Graph, 'B1')
C1_Node_Dictionary = nx.get_node_attributes(my_Graph, 'C1')
print('Node Dictionary of A1: ', A1_Node_Dictionary)
print('Node Dictionary of B1: ', B1_Node_Dictionary)
print('Node Dictionary of C1: ', C1_Node_Dictionary)
print('node list of A1: ', list(A1_Node_Dictionary.values()))
print('node list of B1: ', list(B1_Node_Dictionary.values()))
print('node list of C1: ', list(C1_Node_Dictionary.values()))