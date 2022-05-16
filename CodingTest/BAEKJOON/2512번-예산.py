# 문제 주소 : https://www.acmicpc.net/problem/2512

N = int(input())
arr = list(map(int, input().split()))
M = int(input())

def sum_budget(limit):
    s = 0
    for i in arr:
        s += i if i <= limit else limit
    
    return s

start, end = 0, max(arr)
while start <= end:
    mid = (start + end) // 2

    if sum_budget(mid) > M:
        end = mid - 1
    else:
        start = mid + 1

print( end )