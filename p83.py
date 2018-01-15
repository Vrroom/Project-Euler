import networkx as nx
import numpy as np
import matplotlib.pylab as plt
import time

start_time = time.time()
inp = np.loadtxt('p083_matrix.txt',delimiter=",")
G = nx.DiGraph()
(n,m) = inp.shape
matrix = np.array([[float('inf')]*(m+2)]*(n+2))
matrix[1:n+1,1:m+1] = inp

for i in range(1,n+1):
    for j in range(1,m+1):
        G.add_edge((i-1,j),(i,j),weight=matrix[i][j])
        G.add_edge((i+1,j),(i,j),weight=matrix[i][j])
        G.add_edge((i,j-1),(i,j),weight=matrix[i][j])
        G.add_edge((i,j+1),(i,j),weight=matrix[i][j])


total = nx.dijkstra_path_length(G,(1,1),(n,m)) + matrix[1][1] 
print(total)
print((time.time()-start_time))
