# 문제 주소 : https://www.acmicpc.net/problem/9019

import sys
from queue import deque

def D(n):
    return (2 * n) % 10000

def S(n):
    return n-1 if n != 0 else 9999

def L(n):
    n = str(n)
    return int(n[1:] + n[0])

def R(n):
    n = str(n)
    return int(n[-1] + n[:-1])

T = int(sys.stdin.readline())

for _ in range(T):
    A, B = map(int, sys.stdin.readline().split())
    queue = deque([(A, [])])

    while queue:
        a, log = queue.popleft()
        if a == B:
            print("".join(log))
            break

        queue.append( (D(a), log+['D']) )
        queue.append( (S(a), log+['S']) )
        queue.append( (L(a), log+['L']) )
        queue.append( (R(a), log+['R']) )
            