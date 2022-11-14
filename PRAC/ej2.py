
class Grafo:#creamos la clase grafo
    def __init__(self, vertices):#inicializamos el grafo
        self.vertices = vertices#guardamos el numero de vertices
        self.grafo = [[0 for columna in range(vertices)] for fila in range(vertices)]# Creamos el grafo

    def agregar_arista(self, origen, destino):#agregamos una arista
        self.grafo[origen][destino] = 1# Creamos el grafo

    def orden_topologico(self):#ordenamos el grafo
        visitados = [0] * self.vertices#creamos una lista de visitados
        orden = []#creamos una lista de orden

        for i in range(self.vertices):#recorremos los vertices
            if not visitados[i]:#si no esta visitado
                self.orden_topologico_util(i, visitados, orden)#llamamos a la funcion de ordenamiento

        print(orden)#imprimimos el ordenamiento

    def orden_topologico_util(self, v, visitados, orden):#funcion de ordenamiento
        visitados[v] = 1#marcamos el vertice como visitado

        for i in range(self.vertices):#recorremos los vertices
            if self.grafo[v][i] == 1 and not visitados[i]:#si hay una arista y no esta visitado
                self.orden_topologico_util(i, visitados, orden)#llamamos a la funcion de ordenamiento

        orden.insert(0, v)#insertamos el vertice en el orden
        
        def leer_archivo(self):#funcion para leer el archivo
            with open('aristas.txt', 'r') as archivo:#abrimos el archivo
                for linea in archivo:#recorremos las lineas
                    linea = linea.strip()#quitamos los espacios
                    linea = linea.split()#separamos los elementos
                    self.agregar_arista(int(linea[0]), int(linea[1]))#agregamos la arista
                    
g = Grafo(6)#creamos el grafo

#leer_archivo(g)#leemos el archivo
#agregamos las aristas
g.agregar_arista(5, 4)
g.agregar_arista(1, 4)
g.agregar_arista(2, 3)
g.agregar_arista(1, 3)
g.agregar_arista(1, 5)

g.orden_topologico()#llamamos a la funcion de ordenamiento









