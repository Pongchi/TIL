import sys


limit = 123456 * 2
nLst = [True] * limit
for i in range(2, int(limit ** 0.5)+1):
    if nLst[i] == True:
        for j in range(i+i, limit, i):
            nLst[j] = False

while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break

    print( sum(nLst[n+1:n*2]) if n != 1 else 1)
