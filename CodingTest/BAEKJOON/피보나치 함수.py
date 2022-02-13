'''
import sys

Zero, One = (0, 0)
def fibonacci(n):
    global Zero, One
    if n == 0:
        Zero += 1
        return 0
    elif n == 1:
        One += 1
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

T = int(sys.stdin.readline())
N_lst = tuple( int(sys.stdin.readline()) for i in range(T) )

for i in N_lst:
    Zero, One = (0, 0)
    N = fibonacci(i)
    print(Zero, One, N)
'''
import sys

def fibonacci(n):
    fib = [0, 1]
    if n == 0:
        return print(1, 0)
    elif n == 1:
        return print(0, 1)
        
    for i in range(1, n):
        fib.append(fib[i] + fib[i-1])
    return print(fib[n-1], fib[n])

T = int(sys.stdin.readline())
N_lst = tuple( int(sys.stdin.readline()) for i in range(T) )

for i in N_lst:
    fibonacci(i)
