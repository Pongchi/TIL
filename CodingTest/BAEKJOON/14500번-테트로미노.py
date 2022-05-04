# 문제 주소 : https://www.acmicpc.net/problem/14500

import sys

N, M = map(int, sys.stdin.readline().split())
MAP = [ list(map(int, sys.stdin.readline().split())) for _ in range(N) ]

# 4x4 범위에서 숫자의 합이 가장 높은 구간 찾기.
_max = [0, 0, 0]
for i in range(N-3):
    for j in range(M-3):
        S = sum([ sum([MAP[k][j+l] for l in range(4) ]) for k in range(i, i+4) ])
        if _max[2] < S:
            _max = [i, j, S]

# 찾은 구간을 기준으로 4x4 MAP 자르기.
MAP = [ MAP[i][_max[1]:_max[1]+4] for i in range(_max[0], _max[0]+4) ]

# Brute Force
result = []
## 일직선 도형
for i in range(4):
    result.append( sum(MAP[i]) ) # ㅡ
    resutt.append( sum([ MAP[j][i] for j in range(4) ])) # |

## 정사각형 도형
for i in range(3):
    for j in range(3):
        result.append( sum(MAP[i][j:j+2]) + sum(MAP[i+1][j:j+2]) )

# L자형 도형

        
print( max(result) )