import sys

N = int(sys.stdin.readline())
Meetings = [list(map(int, sys.stdin.readline().split())) for i in range(N) ]
Meetings = sorted(Meetings, key=lambda x : (x[0], x[1]-x[0]))

print(Meetings)
