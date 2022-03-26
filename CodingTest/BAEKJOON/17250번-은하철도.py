# 문제 주소 : https://www.acmicpc.net/problem/17250

# 문제 주소 : https://www.acmicpc.net/problem/4195

import sys

class Set:
    def __init__(self, N, planets_number):
        self.parent = { i:i for i in range(1, N+1) }
        self.number = { i+1:planets_number[i] for i in range(N) }

    def find(self, X):
        if self.parent[X] != X:
            self.parent[X] = self.find(self.parent[X])
        return self.parent[X]
        
    def union(self, A, B):
        A, B = (A, B) if A < B else (B, A)

        A = self.find(A)
        B = self.find(B)

        if A != B:
            self.parent[B] = A
            self.number[A] += self.number[B]

        return self.number[A]
        

N, M = map(int, sys.stdin.readline().split())
planets_number = [ int(input()) for i in range(N) ] 
disjoint_set = Set(N, planets_number)

for m in range(M):
    A, B = map(int, sys.stdin.readline().split())
    print( disjoint_set.union(A, B) )