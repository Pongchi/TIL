# 문제주소 : https://www.acmicpc.net/problem/2004

n, m = map(int, input().split())

def Multi_NtoK(n, k):
    s = n
    for i in range(n+1, k+1):
        s *= i
    return s

def binomial_coefficient(n, m):
    return Multi_NtoK(n-m+1, n) // Multi_NtoK(1, m)

def countZero(n):
    for i in range(len(n)):
        if n[len(n)-1-i] != '0':
            return i

print( countZero(str( binomial_coefficient(n, m) )) )