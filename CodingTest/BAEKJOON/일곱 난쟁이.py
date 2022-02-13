import sys

heights = sorted([int(sys.stdin.readline()) for i in range(9)])
sub = sum(heights) - 100

for i in heights:
    if sub - i in heights:
        print( "\n".join( [ str(heights[x]) for x in range(9) if heights[x] != i and heights[x] != sub - i ] ))
        break
