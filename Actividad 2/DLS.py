

import random

def create_graph(g, m):#Grafo con g nodos y m aristas
    graph = {}
    for i in range(g):
        graph[i] = []
    for i in range(m):
        a = random.randint(0, g - 1)
        b = random.randint(0, g - 1)
        graph[a].append(b)
    return graph

def print_graph(graph): # Imprime el grafo
    for i in graph: 
        print(i, ":", graph[i])
        
        
def DLS(graph, start, goal, limit):#Recorre el grafo en profundidad limitada
    if start == goal:
        return True
    if limit <= 0:
        return False
    for node in graph[start]:
        if DLS(graph, node, goal, limit - 1):
            return True
    return False

def main(): 
    graph = create_graph(10, 20)
    print_graph(graph)
    print(DLS(graph, 0, 9, 2))
    
if __name__ == "__main__":
    main()
    