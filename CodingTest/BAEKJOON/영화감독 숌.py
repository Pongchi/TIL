import sys

N, i, k = int(sys.stdin.readline()), 666, 0

while True:
    if str(i).count("6") >= 3:
        print(i, k)
        k += 1
    
    if N == k:
        print(i)
        break
    i += 1
