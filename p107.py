import networkx as nx
import numpy as np

matrix = np.loadtxt('p107_network.txt',delimiter=",")
G = nx.from_numpy_matrix(matrix)
w = 0
for edge in G.edges():
    w+=G[edge[0]][edge[1]]['weight']
minw = 0
for edge in nx.minimum_spanning_tree(G).edges():
    minw += G[edge[0]][edge[1]]['weight']
print((w-minw))
