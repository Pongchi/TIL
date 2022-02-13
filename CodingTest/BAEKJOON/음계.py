import sys

def Scale(scale):
    print(scale)
    if scale == [1, 2, 3, 4, 5, 6, 7, 8]:
        return "ascending"
    elif scale == [8, 7, 6, 5, 4, 3, 2, 1]:
        return "descending"
    return "mixed"


scale = list(map(int, sys.stdin.readline().split()))
print( Scale(scale) )
