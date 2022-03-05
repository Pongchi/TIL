# 문제 주소 : https://www.acmicpc.net/problem/11727

import sys
sys.setrecursionlimit(10**6)

n = int(input())
arr = [0] + [1, 3] + [0] * (n-2)

def search(n):
    if arr[n] != 0:
        return arr[n]

    arr[n] = search(n-1) + (search(n-2) * 2)
    return arr[n]

print( search(n) % 10007 )