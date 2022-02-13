import sys

def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5+1)):
        if n % i == 0:
            return False
    return True

M, N = map(int, [sys.stdin.readline(), sys.stdin.readline()])
Primes = [i for i in range(M, N+1) if isPrime(i)]

print(f"{sum(Primes)}\n{Primes[0]}" if Primes else -1)
