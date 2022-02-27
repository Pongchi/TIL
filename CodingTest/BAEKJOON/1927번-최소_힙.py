# 문제 주소 : https://www.acmicpc.net/problem/1927

import sys, heapq

arr = []
heapq.heapify(arr)
answer = ""

for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    if n != 0:
        heapq.heappush(arr, n)
    else:
        answer += str(heapq.heappop(arr) if arr else 0) + "\n"
    
print( answer.rstrip()  )