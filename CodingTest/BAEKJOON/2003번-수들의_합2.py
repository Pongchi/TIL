# 문제 주소 : https://www.acmicpc.net/problem/2003

N, M = map(int, input().split())
arr = list(map(int, input().split()))
result = 0

for i in range(N):
    s = 0
    for j in range(i, N):
        if s+arr[j] == M:
            result += 1
            break
        else:
            s += arr[j]

        if s > M:
            break

print( result )