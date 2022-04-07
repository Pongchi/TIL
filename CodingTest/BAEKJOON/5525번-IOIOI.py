# 문제 주소 : https://www.acmicpc.net/problem/5525

N, M, S = int(input()), int(input()), input()
idx = 0
result = 0

while idx < M:
    if S[idx] == 'I':
        PN = 0
        idx += 1
        while idx < M and S[idx:idx+2] == 'OI':
            PN += 1
            idx += 2

        result += PN - N + 1 if PN >= N else 0

    else:
        idx += 1

print(result)