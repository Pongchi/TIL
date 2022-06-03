# 문제 주소 : https://www.acmicpc.net/problem/1049

import math

N, M = map(int, input().split())
sorting1 = sorted([ tuple(map(int, input().split())) for _ in range(M) ], key=lambda x: x[0])
sorting2 = sorted(sorting1, key=lambda x: x[1])

print( min((N//6 * sorting1[0][0]) + (N%6 * sorting2[0][1]),
    math.ceil(N/6) * sorting1[0][0],
    sorting2[0][1] * N) )