# 문제 주소 : https://www.acmicpc.net/problem/2559

N, K = map(int, input().split())
arr = list(map(int, input().split()))
S = sum(arr[:K])
result = S

for i in range(K, N):
    S = S - arr[i-K] + arr[i]
    if result < S:
        result = S

print( result )