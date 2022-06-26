# 문제 주소 : https://www.acmicpc.net/problem/1058

N = int(input())
friends = [0] * N
for _ in range(N):
    for i, v in enumerate(input()):
        if v == 'Y':
            friends[i] += 1

print(max(friends))