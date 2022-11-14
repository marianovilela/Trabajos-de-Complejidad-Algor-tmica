import networkx as nx
import matplotlib.pyplot as plt

def minimo(G, nodos, pesos):
    minimo = float('inf')
    for nodo in nodos:
        if pesos[nodo] < minimo:
            minimo = pesos[nodo]
            nodo_minimo = nodo
    return nodo_minimo

def prim(G, nodo_inicial):

    nodos = list(G.nodes)
    pesos = {}
    for nodo in nodos:
        pesos[nodo] = float('inf')
    pesos[nodo_inicial] = 0
    padre = {}
    padre[nodo_inicial] = None
    arbol = nx.Graph()
    arbol.add_node(nodo_inicial)

    while len(arbol.nodes) < len(G.nodes):
        nodo = minimo(G, nodos, pesos)
        nodos.remove(nodo)
        arbol.add_node(nodo)
        arbol.add_edge(padre[nodo], nodo, weight = pesos[nodo])
        for vecino in G[nodo]:
            if vecino in nodos:
                if G[nodo][vecino]['weight'] < pesos[vecino]:
                    pesos[vecino] = G[nodo][vecino]['weight']
                    padre[vecino] = nodo
    return arbol

G = nx.Graph()

G.add_node('0')
G.add_node('1')
G.add_node('3')
G.add_node('4')
G.add_node('5')
G.add_node('6')
G.add_node('7')

G.add_edge('0', '2', weight = 1)
G.add_edge('1', '2', weight = 3)
G.add_edge('1', '3', weight = 4)
G.add_edge('1', '6', weight = 9)
G.add_edge('2', '4', weight = 3)
G.add_edge('2', '5', weight = 5)
G.add_edge('4', '7', weight = 8)
G.add_edge('5', '6', weight = 9)

pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G, pos, node_size = 500, node_color = 'r')
nx.draw_networkx_edges(G, pos, width = 1)
nx.draw_networkx_labels(G, pos, font_size = 12, font_family = 'sans-serif')
plt.axis('off')
plt.show()


arbol = prim(G, '0')
pos = nx.spring_layout(arbol)
nx.draw_networkx_nodes(arbol, pos, node_size = 500, node_color = 'r')
nx.draw_networkx_edges(arbol, pos, width = 1)
nx.draw_networkx_labels(arbol, pos, font_size = 12, font_family = 'sans-serif')
plt.axis('off')
plt.show()


print(arbol.edges(data = True))