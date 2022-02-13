import sys

N  = int(sys.stdin.readline())
N_dict = dict()
for i in sys.stdin.readline().split():
    if not N_dict.get(i, 0):
        N_dict[i] = 0
    N_dict[i] += 1
    
M = int(sys.stdin.readline())
print( " ".join([ str(N_dict.get(i, 0)) for i in sys.stdin.readline().split()]) )
    
