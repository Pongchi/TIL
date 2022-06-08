# 문제 주소 : https://www.acmicpc.net/problem/16172

S, K = input(), input()

idx = 0
target = 0
while idx < len(S) and target < len(K):
    if not S[idx].isdigit():
        if S[idx] == K[target]:
            target += 1
        else:
            idx -= target
            target = 0
    idx += 1

print( 1 if target == len(K) else 0)
