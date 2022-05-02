# 문제 주소 : https://www.acmicpc.net/problem/1744

N = int(input())
arr = sorted([ int(input()) for _ in range(N) ])
result = 0

while len(arr) > 1:
    a, b = arr.pop(), arr.pop()
    
    if (a <= 0 or b <= 0) or a == b == 1:
        if (a == 0 or b == 0) and arr and arr[-1] < 0:
            result += a if a else b
            arr.pop(0)
        else:
            result += a + b
    
    else:
        result += a*b

print( result + (arr[-1] if arr else 0) )