# 문제 주소 : https://www.acmicpc.net/problem/1010
import sys

def factorial(n):
    s = 1
    for i in range(2, n+1):
        s *= i
    return s

for T in range(int(sys.stdin.readline())):
    N, M = map(int, sys.stdin.readline().split())

    print( factorial(M) // (factorial(N) * factorial(M-N)) )
