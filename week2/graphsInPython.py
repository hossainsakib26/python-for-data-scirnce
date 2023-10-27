import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

G.add_node('A')
G.add_node('B')
G.add_node('C')

G.add_edge('A', 'B')
G.add_edge('B', 'C')
G.add_edge('C', 'A')

nx.draw_networkx(G)
plt.show()