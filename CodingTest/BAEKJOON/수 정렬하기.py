import sys

N = int(sys.stdin.readline())
lst = [int(sys.stdin.readline()) for i in range(N)]

print("\n".join(map(str, sorted(lst))))
