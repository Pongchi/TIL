import sys

N = int(sys.stdin.readline())
N_lst = sys.stdin.readline().split()
M = int(sys.stdin.readline())
M_lst = sys.stdin.readline().split()
TABLE = dict()

for i in N_lst:
    if i not in TABLE:
        TABLE[i] = 0
    TABLE[i] += 1

result = []
for i in M_lst:
    result.append(str(TABLE.get(i, 0)))

print(result)    
print( " ".join(result) )
