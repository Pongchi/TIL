def solution(n, k):
    KN = str(convert(n, k))
    return len([ i for i in KN.split('0') if i != '' and isPrime(int(i)) ])

def isPrime(n):
    if n < 2: return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def convert(n, k):
    if k == 10:
        return n

    tmp = "0123456789"
    q, r = divmod(n, k)
    if q == 0:
        return tmp[r]
    else:
        return convert(q, k) + tmp[r]

print( solution(437674, 3) )
print( solution(110011, 10) )