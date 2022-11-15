# 문제 주소 : https://www.acmicpc.net/problem/9465

for T in range(int(input())):
    n = int(input())
    stamps = [ list(map(int, input().split())), list(map(int, input().split())) ]
    dp = [ [0] * n for _ in range(2) ]
    dp[0][0], dp[1][0] = stamps[0][0], stamps[1][0]
    if n >= 2:
        dp[0][1], dp[1][1] = dp[1][0]+stamps[0][1], dp[0][0]+stamps[1][1]

    for i in range(2, n):
        dp[0][i] = max( dp[1][i-1], dp[0][i-2], dp[1][i-2] ) + stamps[0][i]
        dp[1][i] = max( dp[0][i-1], dp[0][i-2], dp[1][i-2] ) + stamps[1][i]

    print(max(dp[0][-1], dp[1][-1]))