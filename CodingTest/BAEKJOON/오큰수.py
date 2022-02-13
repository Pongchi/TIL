import sys

N = int(sys.stdin.readline())
Lst = tuple( map(int, sys.stdin.readline().split()) )

for idx, num in enumerate(Lst):
    if num == Lst[-1]:
        print(-1)
    for i in Lst[idx+1:]:
        if num < i:
            print(i, end=' ')
            break
        elif i == Lst[-1]:
            print(-1, end=' ')
