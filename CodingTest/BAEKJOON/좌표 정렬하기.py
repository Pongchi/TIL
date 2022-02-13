import sys

N = int(sys.stdin.readline())
lst = [tuple(map(int, sys.stdin.readline().split())) for i in range(N)]

for x, y in sorted(lst, key=lambda x : (x[0], x[1])):
    print(x, y)
