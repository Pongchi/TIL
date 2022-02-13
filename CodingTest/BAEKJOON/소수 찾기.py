import sys

N = int(sys.stdin.readline())
N_lst = { int(i):True for i in sys.stdin.readline().split() }
result = 0

def isPrime(n):
    if n <= 1:
        return False

    for i in range(2, int(n ** 0.5)+1):
        if n % i == 0:
            return False
        
    return True

for i in N_lst:
    if isPrime(i):
        result += 1

print(result)
