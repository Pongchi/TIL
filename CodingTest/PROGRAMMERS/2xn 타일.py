# 문제 주소 : https://programmers.co.kr/learn/courses/30/lessons/12900

def solution(n):
    dp = [0, 1, 2, 3, 5]
    while len(dp) <= n:
        dp.append( dp[-1]+dp[-2] )
    return dp[n]
