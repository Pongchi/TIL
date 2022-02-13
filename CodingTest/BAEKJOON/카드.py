import sys

N = int(sys.stdin.readline())
N_dict = {None:0}
max_n = None

for i in range(N):
    n = int(sys.stdin.readline())
    if n not in N_dict:
        N_dict[n] = 0
    N_dict[n] += 1
    
    if N_dict[max_n] < N_dict[n]:
        max_n = n
        
print(max_n) 
