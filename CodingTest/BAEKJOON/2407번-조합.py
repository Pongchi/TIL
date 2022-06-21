# 문제 주소 : https://www.acmicpc.net/problem/2407

def factorial(n):
    result = 1
    for i in range(2, n+1):
        result *= i
    return result

n, m = map(int, input().split())

print( factorial(n) // (factorial(m) * factorial(n-m)) )