# 문제 주소 : https://www.acmicpc.net/problem/1759

from itertools import combinations

vowels = {'a', 'e', 'i', 'o', 'u'}

L, C = map(int, input().split())
hints = sorted(input().split())

def check(arr):
    v = 0
    c = 0
    for n in arr:
        if n in vowels:
            v += 1
        else:
            c += 1

    return True if v >= 1 and c >= 2 else False

for arr in combinations(hints, L):
    if check(arr):
        print( "".join(arr) )