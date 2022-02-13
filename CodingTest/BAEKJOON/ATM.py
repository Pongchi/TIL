import sys

N = int(sys.stdin.readline())
P_lst = sorted(map(int, sys.stdin.readline().split()))
total = 0
result = []
for i in P_lst:
    total += i
    result.append(total)
    
print( sum(result) )
