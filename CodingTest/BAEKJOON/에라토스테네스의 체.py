import sys

N, K = map(int, sys.stdin.readline().split())
N_lst = [ i for i in range(2, N+1) ]
removed_n = []

while len(removed_n) < K:
    min_n = N_lst.pop(0)
    removed_n.append(min_n)
    N_lst = [ i if i is not None and i % min_n != 0 else removed_n.append(i) for i in N_lst[:] ]
    N_lst = [ i for i in N_lst[:] if i is not None ]
        
print(removed_n[K-1])
    
