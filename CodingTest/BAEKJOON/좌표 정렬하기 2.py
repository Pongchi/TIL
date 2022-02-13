import sys

N = int(sys.stdin.readline())
lst = sorted(enumerate([sys.stdin.readline().split() for i in range(N)]), key=lambda x : (int(x[1][0]), x[0]))
for x in lst:
    print(x[1][0], x[1][1])
