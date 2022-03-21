class disjoint_SET:
    def __init__(self, n):
        self.data = list(range(n))
        self.size = n

    def find(self, index):
        return self.data[index]

    def union(self, x, y):
        x, y = self.find(x), self.find(y)

        if x == y:
            return
        
        for i in range(self.size):
            if self.find(i) == y:
                self.data[i] = x  

    @property
    def length(self):
        return len(set(self.data))

if __name__ == '__main__':
    disjoint = disjoint_SET(10)

    disjoint.union(0, 1)
    disjoint.union(1, 2)
    disjoint.union(2, 3)
    disjoint.union(4, 5)
    disjoint.union(5, 6)
    disjoint.union(6, 7)
    disjoint.union(8, 9)


    print(disjoint.data)
    print(disjoint.length)