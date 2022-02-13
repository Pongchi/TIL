import sys

N = int(sys.stdin.readline())
Lst = { i:0 for i in range(1, 10001) }

for i in range(N):
    Lst[int(sys.stdin.readline())] += 1

Sorted_Lst = tuple( (i, j) for i, j in Lst.items() if j != 0 )

for i, j in Sorted_Lst:
    for k in range(j):
        print(i)
