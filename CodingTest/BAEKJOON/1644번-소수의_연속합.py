# 문제 주소 : https://www.acmicpc.net/problem/1644

N = int(input())
primes = [False, False] + [True] * (N-1)

def isPrime(n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

for i in range(2, N+1):
    if primes[i]:
        for j in range(i+i, N+1, i):
            primes[j] = False

primes_list = [ i for i in range(N+1) if primes[i] ]
print( primes_list )
#################### 시작 ###################
result = 0
for start in range(len(primes_list)):
    total = 0
    for i in range(start, len(primes_list)):
        total += primes_list[i]
        if total == N:
            result += 1
        elif total > N:
            break

print( result )