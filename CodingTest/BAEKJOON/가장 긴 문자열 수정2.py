import sys

L = int(sys.stdin.readline())
S = sys.stdin.readline().rstrip()

TABLE = {}
for i in range(L):
    if TABLE.get(S[i]):
        TABLE[S[i]].append(i)
    else:
        TABLE[S[i]] = [i]

print(TABLE)
