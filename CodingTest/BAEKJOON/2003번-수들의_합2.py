# 문제 주소 : https://www.acmicpc.net/problem/2003

N, M = map(int, input().split())
arr = list(map(int, input().split()))
s, result, end = 0, 0, 0

for start in range(N):
    while s < M and end < N:
        s += arr[end]
        end += 1
    
    if s == M:
        result += 1
    s -= arr[start]

print( result )