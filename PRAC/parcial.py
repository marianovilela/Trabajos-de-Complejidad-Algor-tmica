from collections import deque

def permutaciones(cola, k):
    if k == 1:
        for i in range(len(cola)):
            yield cola[i]
    else:
        for i in range(len(cola)):
            for j in permutaciones(cola, k-1):
                yield cola[i] + j
                
cola = deque()

cola.append('a')
cola.append('b')
cola.append('c')
cola.append('d')

for i in permutaciones(cola, 4):
    print(i)