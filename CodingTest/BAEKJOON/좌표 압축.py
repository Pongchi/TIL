import sys

N = int(sys.stdin.readline())
X_lst = list(map(int, sys.stdin.readline().split()))
X_dict = { x:i for i, x in enumerate(sorted(set(X_lst))) }

print( " ".join([str(X_dict[x]) for x in X_lst]) )
