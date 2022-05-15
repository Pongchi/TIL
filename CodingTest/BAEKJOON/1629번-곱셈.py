# 문제 주소 : https://www.acmicpc.net/problem/1629

def pow(a, b):
    result = 1

    while b > 0:
        if b & 1:
            result *= a
        
        a *= a
        b >>= 1

    return result

A, B, C = map(int, input().split())

print( pow(A, B) % C )