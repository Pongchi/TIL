# 문제 주소 : https://www.acmicpc.net/problem/16435

N, L = map(int, input().split())
fruits = sorted(list(map(int, input().split())))

answer = 0
for fruit in fruits:
    if fruit <= L:
        L += 1
        answer += 1

    else:
        break

print( L )