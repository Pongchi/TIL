# 문제 주소 : https://www.acmicpc.net/problem/12865

import sys

N, K = map(int, sys.stdin.readline().split())
arr = [ tuple(map(int, sys.stdin.readline().split())) for _ in range(N) ]
dp = [ [0]*(K+1) for _ in range(N) ]

for i in range(N):
    for j in range(1, K+1):
        if (j - arr[i][0]) >= 0:
            dp[i][j] = max( dp[i-1][j], dp[i-1][j-arr[i][0]]+arr[i][1] )
        
        else:
            dp[i][j] = dp[i-1][j]

print(dp[-1][-1])