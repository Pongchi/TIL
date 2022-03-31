# 문제 주소 : https://www.acmicpc.net/problem/7662

import sys, heapq

for T in range(int(sys.stdin.readline())):
    heap = []
    for k in range(int(sys.stdin.readline())):
        cmd, value = sys.stdin.readline().split()
        value = int(value)

        if cmd == "I":
            heapq.heappush(heap, value)

        else:
            if heap:
                if value == 1:
                    n = max(heap)
                    heap.remove(n)
                else:
                    n = heapq.heappop(heap)

    print(" ".join(map(str, (max(heap), heapq.heappop(heap)))) if heap else "EMPTY")