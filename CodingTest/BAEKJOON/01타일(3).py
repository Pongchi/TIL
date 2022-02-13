import sys

N = int(sys.stdin.readline())
Lst = [1, 2]

for i in range(N-1):
    Lst.append(Lst[0]+Lst[1])
    Lst.pop(0)

print(Lst)
