#Ejercicio 3
def FordFulkerson(G, s, t):
    #inicializar el grafo residual
    R = {}
    for u in G:
        R[u] = {}
        for v in G[u]:
            R[u][v] = G[u][v]
    f = 0
    #mientras exista un camino aumentante
    while True:
        #encontrar un camino aumentante
        P, d = BFS(R, s, t)
        if P == None:
            break
        #determinar el valor del flujo aumentante
        df = min([R[u][v] for u,v in P])
        #actualizar el flujo
        for u,v in P:
            R[u][v] -= df
            R[v][u] += df
        f += df
    return f, R

def BFS(G, s, t):
    #inicializar la cola
    Q = [s]
    
    P = {s:None}
    #mientras la cola no esté vacía
    while len(Q) > 0:
        #extraer un nodo de la cola
        u = Q.pop(0)
        #para cada vecino v de u
        for v in G[u]:
            #si el peso de la arista (u,v) es mayor a cero
            #y v no ha sido visitado
            if G[u][v] > 0 and v not in P:
                #marcar a v como visitado
                P[v] = u
                #si v es el nodo sumidero
                if v == t:
                    #retornar el camino aumentante y su valor
                    return path(P, s, t), G[u][v]
                #agregar v a la cola
                Q.append(v)
    #no existe un camino aumentante
    return None, None

def path(P, s, t):
    C = []
    u = t
    while u != s:
        #agregar el nodo actual al camino
        C.append((P[u], u))
        #actualizar el nodo actual
        u = P[u]
    #retornar el camino
    return C[::-1]
G = {
    's': {'w': 4, 'x': 7,'z':10},
    'w': {'y': 2, 't': 10},
    'x': {'w': 2, 'y': 10,'z':2},
    'z': {'y': 2,'t':6},
    'y': {'t': 7},
    't': {}
}
s = 's'
t = 't'
f, R = FordFulkerson(G, s, t)
print('Flujo máximo:', f)