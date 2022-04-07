# 문제 주소 : https://www.acmicpc.net/problem/5525

N, M, S = int(input()), int(input()), input()
Pn = "IO" * N + "I"
idx = 0
result = 0

while idx < M:
    if S[idx] == 'I' and S[idx:idx+len(Pn)] == Pn:
        result += 1
        idx += 2

    else:
        idx += 1

print(result)