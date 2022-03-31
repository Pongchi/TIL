# 문제 주소 : https://www.acmicpc.net/problem/7662

import sys, heapq

for T in range(int(sys.stdin.readline())):
    print("========================")
    max_heap = []
    min_heap = []
    for k in range(int(sys.stdin.readline())):
        cmd, value = sys.stdin.readline().split()
        value = int(value)

        if cmd == "I":
            heapq.heappush(max_heap, -value)
            heapq.heappush(min_heap, value)
        
        else:
            if max_heap and min_heap:
                tmp = []
                if value == 1:
                    n = heapq.heappop(max_heap)
                    while (min_heap):
                        tmp.append(heapq.heappop(min_heap))
                        if tmp[-1] == n:
                            for i in tmp[:-1]:
                                heapq.heappush(min_heap, i)
                            break
                else:
                    n = heapq.heappop(min_heap)
                    while (max_heap):
                        tmp.append(heapq.heappop(max_heap))
                        if tmp[-1] == n:
                            for i in tmp[:-1]:
                                heapq.heappush(max_heap, i)
                            break    
  
    if max_heap:
        print(-heapq.heappop(max_heap), heapq.heappop(min_heap))

    else:
        print("EMPTY")