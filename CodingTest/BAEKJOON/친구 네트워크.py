import sys

T = int(sys.stdin.readline())

for t in range(T):
    F = int(sys.stdin.readline())
    F_network = set()

    for f in range(F):
        F_network = F_network.union(set(sys.stdin.readline().split()))
        print(len(F_network))
