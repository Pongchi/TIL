# 문제 주소 : https://www.acmicpc.net/problem/901
# PyPy3

import sys
from queue import deque

def D(n):
    return (2 * n) % 10000

def S(n):
    return n-1 if n != 0 else 9999

def L(n):
    return (n % 1000) * 10 + n // 1000

def R(n):
    return (n % 10) * 1000 + n // 10

T = int(sys.stdin.readline())
for _ in range(T):
    A, B = map(int, sys.stdin.readline().split())
    queue = deque([(A, '')])
    visited = [0] * 10000

    while queue:
        a, log = queue.popleft()
        if a == B:
            print(log)
            break
        
        n = D(a)
        if not visited[n]:
            visited[n] = 1
            queue.append( (n, log+'D') )
        n = S(a)
        if not visited[n]:
            visited[n] = 1
            queue.append( (n, log+'S') )
        n = L(a)
        if not visited[n]:
            visited[n] = 1
            queue.append( (n, log+'L') )
        n = R(a)
        if not visited[n]:
            visited[n] = 1
            queue.append( (n, log+'R') )