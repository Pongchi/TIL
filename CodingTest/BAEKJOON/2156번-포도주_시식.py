# 문제 주소 : https://www.acmicpc.net/problem/2156

grape = [ int(input()) for n in range(int(input())) ]
dp = [0] * len(grape)

dp[0] = grape[0]
if len(grape) > 1:
    dp[1] = dp[0] + grape[1]
    if len(grape) > 2:
        dp[2] = max(dp[1], dp[0]+grape[2], grape[1]+grape[2])

for i in range(3, len(grape)):
    dp[i] = max(dp[i-1], dp[i-2]+grape[i], dp[i-3]+grape[i]+grape[i-1])

print(dp[-1])