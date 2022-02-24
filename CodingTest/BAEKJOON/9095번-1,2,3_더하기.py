# 문제 주소 : https://www.acmicpc.net/problem/9095

import sys
sys.setrecursionlimit(10**6)

arr = [0, 1, 2, 4] + [0] * (11 - 3)
def search(n):
    if arr[n] != 0:
        return arr[n]

    arr[n] = search(n-1) + search(n-2) + search(n-3)
    return arr[n]

for t in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    print( search(n) )

