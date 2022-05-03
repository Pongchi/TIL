# 문제 주소 : https://www.acmicpc.net/problem/2193

N = int(input())
a, b = 1, 1
for i in range(N-1):
    a, b = b, a+b

print(a)