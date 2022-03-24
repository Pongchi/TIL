# 문제 주소 : https://www.acmicpc.net/problem/4195

import sys

class Set:
    def __init__(self):
        self.parent = dict()
        self.number = dict()

    def initialize(self, X):
        if not X in self.parent:
            self.parent[X] = X
            self.number[X] = 1

    def find(self, X):
        if self.parent[X] != X:
            self.parent[X] = self.find(self.parent[X])
        return self.parent[X]
        
    def union(self, A, B):
        self.initialize(A)
        self.initialize(B)

        A, B = (A, B) if A < B else (B, A)

        A = self.find(A)
        B = self.find(B)

        if A != B:
            self.parent[B] = A
            self.number[A] += self.number[B]

        return self.number[A]
        
T = int(sys.stdin.readline())
for t in range(T):
    F = int(sys.stdin.readline())
    disjoint_set = Set()
    result = []
    for f in range(F):
        A, B = sys.stdin.readline().split()
        result.append(disjoint_set.union(A, B))
    print("\n".join(map(str, result)))