# 문제 주소 : https://www.acmicpc.net/problem/5430

import sys
from queue import deque

def AC(p, n, arr):
    rev = False

    for cmd in p:
        if cmd == 'R':
            rev = not rev
        else:
            if not arr:
                return "error"
    
            if rev:
                arr.pop()
            else:
                arr.popleft()

    return '[' + ','.join(map(str, arr if not rev else reversed(arr))) + ']'

for T in range(int(sys.stdin.readline())):
    p = sys.stdin.readline().rstrip()
    n = int(sys.stdin.readline())
    arr = sys.stdin.readline()[1:-2].split(',')
    arr = deque(list(map(int, arr))) if arr[0] else deque([])

    print( AC(p, n, arr) )