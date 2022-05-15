# 문제 주소 : https://www.acmicpc.net/problem/10872

def factorial(n):
    if n == 0:
        return 1

    elif n <= 1:
	    return n

    return factorial(n-1) * n

N = int(input())

print( factorial(N) )