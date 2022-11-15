# 문제 주소 : https://www.acmicpc.net/problem/9465

def dp(score, loc):
    if loc[1] > n-1:
        return score

    score += stamps[loc[0]][loc[1]]
    return max( dp(score, (0 if loc[0] else 0, loc[1]+1)),  dp(score, (0, loc[1]+2)), dp(score, (1, loc[1]+2)) )

for T in range(int(input())):
    n = int(input())
    stamps = [ list(map(int, input().split())), list(map(int, input().split())) ]

    print("정답 :", max( dp(0, (0,0)), dp(0, (1, 0)) ))