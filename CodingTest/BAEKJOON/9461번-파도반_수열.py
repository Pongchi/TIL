# 문제 주소 : https://www.acmicpc.net/problem/9461

seq = [0, 1, 1, 1, 2, 2, 3, 4, 5, 7, 9]
def dp(N):
    while len(seq) <= N:
        seq.append(seq[-1]+seq[-5])

    return seq[N]

for T in range(int(input())):
    print( dp(int(input())) )