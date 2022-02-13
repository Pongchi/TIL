import sys

def drawStar(n):
    if n == 1:
        return ['*']
    STAR = drawStar(n//3)
    L = []

    for s in STAR:
        L.append(s*3)
    for s in STAR:
        L.append(s + " "*(n//3) + s)
    for s in STAR:
        L.append(s*3)

    print(STAR, L)
    return L

n= int(sys.stdin.readline())
print( '\n'.join(drawStar(n)) )
