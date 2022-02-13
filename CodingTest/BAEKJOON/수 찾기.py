import sys

N = int(sys.stdin.readline())
N_dict = { i:1 for i in sys.stdin.readline().split() }

M = int(sys.stdin.readline())

for m in sys.stdin.readline().split():
    print( N_dict.get(m, 0) )