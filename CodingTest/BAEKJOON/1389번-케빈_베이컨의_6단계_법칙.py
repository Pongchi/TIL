# 문제 주소 : https://www.acmicpc.net/problem/1389

import sys
from math import inf

N, M = map(int, sys.stdin.readline().split())
relation = [[inf] * N for _ in range(N)]

for _ in range(M):
    A, B = map(int, sys.stdin.readline().split())
    relation[A-1][B-1] = 1
    relation[B-1][A-1] = 1

for k in range(N):
    relation[k][k] = 0
    for i in range(N):
        for j in range(N):
            relation[i][j] = min(relation[i][j], relation[i][k]+relation[k][j])

S = []
result = 0
for i in range(N):
    s = sum([ j for j in relation[i] if j != inf ])
    S.append(s)
    if s != 0 and s < S[result]:
        result = i

print( result+1 )