import sys

class disjoint_SET:
    def __init__(self, n):
        self.data = list(range(n+1))
        self.size = n

    def find(self, index):
        return self.data[index]

    def isInclude(self, x, y):
        return "YES" if self.find(x) == self.find(y) else "NO"

    def union(self, x, y):
        x, y = self.find(x), self.find(y)

        if x == y:
            return
        
        self.data[y] = x  

    @property
    def length(self):
        return len(set(self.data))

n, m = map(int, sys.stdin.readline().split())

SET = disjoint_SET(n)
for operator in range(m):
    cmd, a, b = map(int, sys.stdin.readline().split())

    if cmd == 0:
        SET.union(a, b)
    else:
        print( SET.isInclude(a, b))