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
        
def UCS(graph, start, goal):#Recibe el grafo, el nodo inicial y el nodo final
    if start == goal:
        return True
    for node in graph[start]:
        if UCS(graph, node, goal):
            return True
    return False

def main():
    
    graph = create_graph(10, 20)
    print_graph(graph)
    print(UCS(graph, 0, 9))

if __name__ == "__main__":
    main()
