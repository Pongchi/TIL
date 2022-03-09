# 문제 주소 : https://www.acmicpc.net/problem/11286

import sys
from queue import PriorityQueue

arr = PriorityQueue()
size = 0
result = []
for _ in range(int(sys.stdin.readline())):
    x = int(sys.stdin.readline())
    if x != 0:
        arr.put((abs(x), x))
        size += 1

    else:
        if size:
            n = arr.get()
            size -= 1
            result.append(n[1])
        else:
            result.append(0)

print( "\n".join(map(str, result)))