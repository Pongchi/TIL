# 문제 주소 : https://www.acmicpc.net/problem/1676

N = int(input())

f = 1
for i in range(2, N+1):
    f *= i

result = 0
for n in str(f)[::-1]:
    if n != '0':
        break
    result += 1

print( result )