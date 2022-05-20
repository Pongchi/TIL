# 문제 주소 : https://www.acmicpc.net/problem/3273

n = int(input())
arr = sorted(map(int, input().split()))
x = int(input())
result = 0

for i in range(n-1):
    if arr[i]+arr[i+1] > x:
        break

    for j in range(i+1, n):
        s = arr[i]+arr[j]
        if s == x:
            result += 1
        elif s > x:
            break

print( result )