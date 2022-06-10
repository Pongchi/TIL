# 문제 주소 : https://www.acmicpc.net/problem/6588

import sys

_max = 1000000 + 1
primes = [True] * _max
primes[0], primes[1] = False, False
for i in range(2, _max):
    if primes[i]:
        for j in range(i*2, _max, i):
            primes[j] = False

while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break

    if n & 1:
        print("Goldbach's conjecture is wrong.")
    else:
        for i in range(3, n, 2):
            if primes[i] and primes[n-i]:
                print(f"{n} = {i} + {n-i}")
                break
        else:
            print("Goldbach's conjecture is wrong.")