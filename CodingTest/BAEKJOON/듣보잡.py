import sys

N, M = map(int, sys.stdin.readline().split())
non_Heard = set()
non_Seen = set()

for n in range(N):
    non_Heard.add(sys.stdin.readline().rstrip())
for m in range(M):
    non_Seen.add(sys.stdin.readline().rstrip())
    
NaN = non_Heard & non_Seen
print(len(NaN))
print( "\n".join(sorted(NaN)) )
