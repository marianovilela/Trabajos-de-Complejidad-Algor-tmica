import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
G=nx.DiGraph()
G.add_nodes_from([0,1,2,3])
G.add_edges_from([(1,2),(1,3),(3,1),(1,1),(2,1)])
nx.draw(G, with_labels=True)
plt.show()

def dfs(G, ini,fin):
    visited = []
    stack = [ini]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.append(vertex)
            if vertex == fin:
                break
            stack.extend(set(G[vertex]) - set(visited))
    return visited

print(dfs(G,3,2))