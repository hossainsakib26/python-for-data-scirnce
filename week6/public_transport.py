import networkx as nx
import matplotlib.pyplot as plt

#create object of graph
my_Graph = nx.Graph()

#add nodes/points on a graph
#jubili line
my_Graph.add_node('A', npos=(10,25), ccn='#4a4141') #stratford
plt.text(x=10, y=25, s='Stratford', rotation=15)
my_Graph.add_node('B', npos=(20,20), ccn='#4a4141') #westhum [value = 20]
plt.text(x=20, y=20, s='Westhum', rotation=15)
my_Graph.add_node('C', npos=(30,55), ccn='#4a4141') #canning town
plt.text(x=30, y=55, s='Canning Town', rotation=15)
my_Graph.add_node('D', npos=(50,50), ccn='#4a4141') #canary warf [value = 50]
plt.text(x=50, y=50, s='Canary warf', rotation=15)

#add lines to connect nodes on a graph
my_Graph.add_edge('A', 'B', cce='#9F9F9F')
my_Graph.add_edge('B', 'C', cce='#9F9F9F')
my_Graph.add_edge('C', 'D', cce='#9F9F9F')

#aset attributes to jubili line
#nx.set_node_attributes(my_Graph, {'A': 10, 'B': 20, 'C': 30, 'D': 50}, name='A1')

#add nodes/points on a graph
#city line
my_Graph.add_node('E', npos=(35,35), ccn='#ad4546') #Illford
plt.text(x=35, y=35, s='Illford', rotation=15)
my_Graph.add_node('F', npos=(25,50), ccn='#ad4546') #Barking
plt.text(x=25, y=50, s='Barking', rotation=15)
my_Graph.add_node('G', npos=(35,60), ccn='#ad4546') #Eastham
plt.text(x=35, y=60, s='Eastham', rotation=15)
my_Graph.add_node('H', npos=(60,75), ccn='#ad4546') #Plaisto
plt.text(x=60, y=75, s='Plaisto', rotation=15)
my_Graph.add_node('I', npos=(20,20), ccn='#ad4546') #Westhum [value = 20]
plt.text(x=20, y=20, s='Westhum', rotation=15)

#add lines to connect nodes on a graph
my_Graph.add_edge('E', 'F', cce='#DC0102')
my_Graph.add_edge('F', 'G', cce='#DC0102')
my_Graph.add_edge('G', 'H', cce='#DC0102')
my_Graph.add_edge('H', 'I', cce='#DC0102')

#add nodes/points on a graph
#DLR line
my_Graph.add_node('J', npos=(85, 20), ccn='#00AFAA') #Bow Charch
plt.text(x=85, y=20, s='Bow Charch', rotation=15)
my_Graph.add_node('K', npos=(75, 45), ccn='#00AFAA') #Polar
plt.text(x=75, y=45, s='Polar', rotation=15)
my_Graph.add_node('L', npos=(65, 55), ccn='#00AFAA') #West india Quay
plt.text(x=65, y=55, s='West india Quay', rotation=15)
my_Graph.add_node('M', npos=(50, 50), ccn='#00AFAA') #canary Warf [value = 50]
plt.text(x=50, y=50, s='canary Warf', rotation=15)

#add lines to connect nodes on a graph
my_Graph.add_edge('J', 'K', cce='#000F9F')
my_Graph.add_edge('K', 'L', cce='#000F9F')
my_Graph.add_edge('L', 'M', cce='#000F9F')

#nx.set_node_attributes(my_Graph, {'J': 85, 'K': 75, 'L': 65, 'M': 50}, name='C1')
#extract attribute from the graph dictionary
node_position = nx.get_node_attributes(my_Graph, 'npos') #position of all nodes
print('positions of nodes: ',node_position)
node_Color = nx.get_node_attributes(my_Graph, 'ccn')
print('color of node positions: ', node_Color)
edge_Color = nx.get_edge_attributes(my_Graph, 'cce')
print('color of edge: ', edge_Color)
print('-----------------------------------------------------------')
print(list(node_position.values()))
node_color_list = list(node_Color.values())
print(node_color_list)
edge_Color_list = list(edge_Color.values())
print(edge_Color_list)

#now its time to draw graph
nx.draw_networkx(my_Graph, node_position, node_color=node_color_list)
nx.draw_networkx_edges(my_Graph, node_position, edge_color=edge_Color_list)

#visualise the graph
plt.show()