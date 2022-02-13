import sys

def gcd(m ,n):
    while True:
        r = m - (n * (m//n))
        m = n
        n = r
        if r == 0:
            return m

def lcm(m, n, gcd):
    return (m*n) // gcd 

a, b = sorted(map(int, sys.stdin.readline().split()))

GCD = gcd(b, a)
print(GCD)
LCM = lcm(b, a, GCD)
print(LCM)
