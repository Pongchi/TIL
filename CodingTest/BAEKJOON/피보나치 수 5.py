import sys

Fib = {0:0, 1:1}
def Fibonacci(n):
    if n in Fib:
        return Fib[n]
    
    Fib[n] = Fibonacci(n-1) + Fibonacci(n-2)
    return Fib[n]

n = int(sys.stdin.readline())
print( Fibonacci(n) )
