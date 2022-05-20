# 문제 주소 : https://www.acmicpc.net/problem/3273

n = int(input())
arr = sorted(map(int, input().split()))
x = int(input())
result, end = 0, 1

for start in range(n-1):
    while arr[start] + arr[end] < x and end < n-1:
        end += 1

    if start >= end:
        break
    if arr[start]+arr[end] == x:
        result += 1
        
    end -= 1

print( result )