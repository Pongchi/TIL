# 문제 주소 : https://www.acmicpc.net/problem/16953
    
from queue import deque

A, B = map(int, input().split())

q = deque([(A, 1)])

while q:
    n, i = q.popleft()
    
    if n == B:
        print(i)
        exit()
    
    elif n < B:
        q.append( (n*2, i+1) )
        q.append( (int(str(n)+'1'), i+1))

print(-1)