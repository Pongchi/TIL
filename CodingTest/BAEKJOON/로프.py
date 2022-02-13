import sys

N = int(sys.stdin.readline())
Rope = sorted([int(sys.stdin.readline()) for i in range(N)], reverse=True)
rope = []
result = []
for r in Rope:
    rope.append(r)
    result.append(rope[-1]*len(rope))

print( max(result) )
