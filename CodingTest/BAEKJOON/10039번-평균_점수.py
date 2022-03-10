# 문제 주소 : https://www.acmicpc.net/problem/10039

total = 0
for i in range(5):
    n = int(input())
    total += n if n >= 40 else 40

print( total // 5)