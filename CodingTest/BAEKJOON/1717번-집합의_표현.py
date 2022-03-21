import sys

class Set:
    def __init__(self,N):
        self.S = [-1 for _ in range(N+1)]
        self.size = N+1
        
    def find(self, i):
        set_num = self.S[i]
        if set_num < 0:
            return i
        else:
            return self.find(set_num)
        
    def union(self, i, j):
        i_root = self.find(i)
        j_root = self.find(j)
        if i_root != j_root:
            if self.S[i_root] < self.S[j_root]:
                self.S[j_root] = i_root
            elif self.S[i_root] > self.S[j_root]:
                self.S[i_root] = j_root
            else:
                self.S[i_root] -= 1
                self.S[j_root] = i_root
            self.size -= 1

    def isInclude(self, i, j):
        return "YES" if self.find(i) == self.find(j) else "NO"

n, m = map(int, sys.stdin.readline().split())

SET = Set(n)
for operator in range(m):
    cmd, a, b = map(int, sys.stdin.readline().split())
    
    if cmd == 0:
        SET.union(a, b)
    else:
        print( SET.isInclude(a, b))