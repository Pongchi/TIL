# 문제 주소 : https://www.acmicpc.net/problem/1712

A, B, C = map(int, input().split())

if B < C:
    S = A + B
    result = 1

    while S >= result * C:
        S += B
        result += 1

    print( result )
else:
    print(-1)