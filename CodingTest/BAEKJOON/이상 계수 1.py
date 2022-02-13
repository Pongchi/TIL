import sys

dic = {0:0, 1:1, 2:2}
def factorial(n):
    if n in dic:
        return dic[n]
    
    dic[n] = factorial(n-1) * n
    return dic[n]

N, K = map(int, sys.stdin.readline().split())
try:
    result = factorial(N) // (factorial(K) * factorial(N-K))
except ZeroDivisionError:
    result = 1

print( result )
