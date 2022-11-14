'''
Ejercicio 1: UFDS
Resolver este problema requiere implementar las funciones básicas y probar su complejidad sobre casos
prácticos.
Ejercicio 1.1
Implemente las funciones Find y Union.
'''
class UFDS:
    def __init__(self, n):
        self.p = [i for i in range(n)]
        self.rank = [0 for i in range(n)]

    def find(self, i):
        if self.p[i] == i:
            return i
        else:
            self.p[i] = self.find(self.p[i])
            return self.p[i]

    def union(self, i, j):
        x = self.find(i)
        y = self.find(j)
        if x == y:
            return
        if self.rank[x] > self.rank[y]:
            self.p[y] = x
        else:
            self.p[x] = y
            if self.rank[x] == self.rank[y]:
                self.rank[y] += 1
                
    def sameSet(self, i, j):
        
        return self.find(i) == self.find(j)
     
    def numDisjointSets(self):
        
        return len(set(self.p))
    
    def sizeOfSet(self, i):
        return self.p.count(self.find(i))
     
    def print(self):
        print(self.p)
        print(self.rank)
        
if __name__ == '__main__':
    
    n = int(input())
    ufds = UFDS(n)
    while True:
        try:
            line = input()
            if line == '':
                break
            line = line.split()
            if line[0] == 'c':
                ufds.union(int(line[1]), int(line[2]))
            elif line[0] == 'q':
                print(ufds.sameSet(int(line[1]), int(line[2])))
        except EOFError:
            break
        
    print(ufds.numDisjointSets(), 'components')
    
    for i in range(n):
        
        print('Size of component', i, 'is', ufds.sizeOfSet(i))
        
    ufds.print()
