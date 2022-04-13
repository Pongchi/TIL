# 문제 주소 : https://www.acmicpc.net/problem/11055

N = int(input())
A = list(map(int, input().split()))

dp = [0] * 1001
for i in A:
    dp[i] = max(dp[:i]) + i

print( max(dp) )