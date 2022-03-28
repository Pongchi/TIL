# 문제 주소 : https://www.acmicpc.net/problem/17626

n = int(input())
dp = [0, 1]

for i in range(2, n+1):
    _min = 50001
    j = 1

    while j**2 <= i:
        _min = min(_min, dp[i-(j**2)])
        j += 1

    dp.append(_min+1)

print(dp[n])