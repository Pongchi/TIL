# 문제 주소 : https://www.acmicpc.net/problem/1629

def pow(a, b):
    if b == 0:
        return 1

    elif b % 2 == 0:
        n = pow(a, b // 2)
        return n*n
    
    else:
        n = pow(a, (b-1)//2)
        return a * n * n

A, B, C = map(int, input().split())

print( pow(A, B) % C )