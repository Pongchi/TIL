import heapq

def solution(operations):
    heap = []
    for operation in operations:
        cmd, value = operation.split()
        value = int(value)
    
        if cmd == "I":
            heapq.heappush(heap, value)

        else:
            if heap:
                if value == 1:
                    heap.remove(heapq.nlargest(1, heap)[0])
                else:
                    heapq.heappop(heap)
    
    return [max(heap), heapq.heappop(heap)] if heap else [0, 0]