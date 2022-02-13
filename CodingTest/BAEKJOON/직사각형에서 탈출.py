import sys

x, y, w, h = map(int, sys.stdin.readline().split())
distance = [x, y, w-x, h-y]

print( min(distance) )