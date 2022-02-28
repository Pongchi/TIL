# 문제 주소 : https://www.acmicpc.net/problem/9184

import sys

memo = {}

def w(a, b, c):
    memorize = memo.get((a, b, c), False)
    if memorize:
        return memorize
    
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    
    if a > 20 or b > 20 or c > 20:
        memo[(20, 20, 20)] = w(20, 20, 20)
        return memo[(20, 20, 20)]
        
    
    if a < b and b < c:
        memo[(a, b, c)] =  w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
        return memo[(a, b, c)]
    
    memo[(a, b, c)] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
    return memo[(a, b, c)]

while True:
    a, b, c = map(int, sys.stdin.readline().split())
    if a == b == c == -1:
        break
    
    print(f'w({a}, {b}, {c}) = {w(a,b,c)}')