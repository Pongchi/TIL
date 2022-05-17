# 문제 주소 : https://www.acmicpc.net/problem/9019

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
    queue = deque([(A, [])])
    visited = [1] * 10000

    while queue:
        a, log = queue.popleft()
        if a == B:
            print("".join(log))
            break
        
        if visited[a]:
            visited[a] = 0
            if a == 0:
                queue.append( (S(a), log+['S']) )
            
            else:
                queue.append( (D(a), log+['D']) )
                queue.append( (S(a), log+['S']) )
                queue.append( (L(a), log+['L']) )
                queue.append( (R(a), log+['R']) )