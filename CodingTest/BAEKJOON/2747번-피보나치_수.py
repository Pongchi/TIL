# 문제 주소 : https://www.acmicpc.net/problem/2747

n = int(input())
a, b = 1, 1

for i in range(n-1):
    a, b = b, a+b

print(a)