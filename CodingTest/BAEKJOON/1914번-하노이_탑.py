N = int(input())

def hanoi(n, pos1, tmp, pos2):
    if n == 1:
        print(pos1, pos2)
    else:
        hanoi(n-1, pos1, pos2, tmp)
        print(pos1, pos2)
        hanoi(n-1, tmp, pos1, pos2)

print(2**N-1)
if N <= 20:
    hanoi(N, 1, 2, 3)