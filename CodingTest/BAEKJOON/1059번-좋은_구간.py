# 문제 주소 : https://www.acmicpc.net/problem/1059

L = int(input())
S = sorted(map(int, input().split()))
n = int(input())

if (S[0] > n) or (n in S):
    print(0)
    exit(0)

for i in range(L):
    if n < S[i]:
        print(S[i]-S[i-1])
        break