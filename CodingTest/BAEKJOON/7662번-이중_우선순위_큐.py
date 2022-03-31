# 문제 주소 : https://www.acmicpc.net/problem/7662

import sys, heapq

for T in range(int(sys.stdin.readline())):
    min_heap = []
    max_heap = []
    for k in range(int(sys.stdin.readline())):
        cmd, value = sys.stdin.readline().split()
        value = int(value)

        if cmd == "I":
            heapq.heappush(min_heap, value)
            heapq.heappush(max_heap, -value)

        else:
            if max_heap:
                if value == 1:
                    n = heapq.heappop(max_heap)
                    min_heap.remove(-n)
                else:
                    n = heapq.heappop(min_heap)
                    max_heap.remove(-n)

    print(" ".join(map(str, (-heapq.heappop(max_heap), heapq.heappop(min_heap)))) if max_heap else "EMPTY")