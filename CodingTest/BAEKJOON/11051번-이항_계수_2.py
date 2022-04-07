# 문제 주소 : https://www.acmicpc.net/problem/11051
def binomial_coefficient(n, k):
    dp = [ [0]*(k+1) for i in range(n+1) ]

    for N in range(n+1):
        for K in range(min(N, k)+1):
            if K == 0 or N == K:
                dp[N][K] = 1
            else:
                dp[N][K] = dp[N-1][K-1] + dp[N-1][K]
    
    return dp[N][K]

N, K = map(int, input().split())

print( binomial_coefficient(N, K) % 10007 )