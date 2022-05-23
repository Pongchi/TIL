# 문제 주소 : https://www.acmicpc.net/problem/3273

n = int(input())
arr = sorted(map(int, input().split()))
x = int(input())
result, start, end = 0, 0, n-1

while start != end:
    S = arr[start]+arr[end]
    if S == x:
        result += 1
        start += 1

    elif S > x:
        end -= 1
    
    else:
        start += 1

print( result )