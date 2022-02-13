import sys

M, N = map(int, sys.stdin.readline().split())
LIST = {i:True for i in range(M, N+1)}
    
def isPrime(n):
    if n <= 1:
        return False
    
    for i in range(2, int(n ** 0.5)+1):
        if n % i == 0:
            return False
    return True

for n in range(M, N+1):
    if not LIST[n]:
        continue
        
    if isPrime(n):
        print(n)

        i = 1
        while n * i <= N:
            if LIST[n * i]:
                LIST[n * i] = False

            i += 1
