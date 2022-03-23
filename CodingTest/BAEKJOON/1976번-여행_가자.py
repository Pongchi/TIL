import sys

class Set:
    def __init__(self,N):
        self.S = [-1 for _ in range(N+1)]
        self.size = N
        
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

N, M = map(int, [sys.stdin.readline(), sys.stdin.readline()])
MAP = [ list(map(int, sys.stdin.readline().split())) for _ in range(N) ]
plan = list(map(lambda x: int(x)-1, sys.stdin.readline().split()))
disjoint_set = Set(N)

for i in range(N):
    for j in range(i+1, N):
        if MAP[i][j]:
            disjoint_set.union(i, j)

print("YES" if disjoint_set.find(plan[0]) == disjoint_set.find(plan[-1]) else "NO")
