import sys

T = int(sys.stdin.readline())

for t in range(T):
    N, N = sys.stdin.readline(), { i:1 for i in sys.stdin.readline().split() }
    M = sys.stdin.readline()
    for i in sys.stdin.readline().split():
        print(N.get(i, 0))
