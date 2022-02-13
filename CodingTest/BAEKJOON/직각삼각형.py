import sys

while True:
    length = sorted(map(int, sys.stdin.readline().split()))
    if length[0] == length[1] == length[2] == 0:
        break

    print( "right" if length[2] ** 2 == length[0] ** 2 + length[1] ** 2 else "wrong" )
