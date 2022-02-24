# 문제 주소 : https://www.acmicpc.net/problem/2579

import sys

'''
N = int(sys.stdin.readline())
stair = [0] + [ int(sys.stdin.readline()) for _ in range(N) ]
memo = [0] * (N+1)
memo[1] = stair[1]
if N >= 2:
    memo[2] = memo[1] + stair[2]
    if N >= 3:
        memo[3] = stair[1] + stair[3]

def dp(n):
    if memo[n] != 0:
        return memo[n]

    memo[n] = max(dp(n-3) + stair[n-1],  dp(n-2)) + stair[n]
    return memo[n]

print(dp(N))
'''

n = int(input())
stair = [0] + [int(input()) for _ in range(n)]

if n == 1:
    print(stair[-1])

else:
    dp = [0] * (n + 1)
    dp[0] = stair[0]
    dp[1] = max(stair[0] + stair[1], stair[1])
    dp[2] = max(stair[0] + stair[2], stair[1] + stair[2])
    for i in range(3, n + 1):
        dp[i] = max(dp[i - 2] + stair[i], dp[i - 3] + stair[i - 1] + stair[i])
        
    print(dp[-1])