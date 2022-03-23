import sys

class Set:
    def __init__(self,N):
        self.S = [-1] * N
        
    def find(self, i):
        if self.S[i] < 0:
            return i
        return self.find(self.S[i])
        
    def union(self, i, j):
        i = self.find(i)
        j = self.find(j)

        if i == j:
            return
        
        if self.S[i] <= self.S[j]:
            self.S[j] = i
        else:
            self.S[i] = j

N, M = map(int, [sys.stdin.readline(), sys.stdin.readline()])
MAP = [ list(map(int, sys.stdin.readline().split())) for _ in range(N) ]

plan = []
for p in map(lambda x: int(x)-1, sys.stdin.readline().split()):
    if plan and plan[-1] == p:
        clash += 1
        continue
    plan.append(p)

disjoint_set = Set(N)
for i in range(N):
    for j in range(N):
        if MAP[i][j]:
            disjoint_set.union(i, j)

result = [ disjoint_set.find(i) for i in plan ]
print("YES" if len(set(result)) == 1 else "NO")