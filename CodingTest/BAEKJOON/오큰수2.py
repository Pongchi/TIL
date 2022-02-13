import sys

N = int(sys.stdin.readline())
Seq = tuple( map(int, sys.stdin.readline().split()) )
stack = []

for i in range(len(stack), N):
    for j in range(len(stack)+1, N):
        if Seq[i] < Seq[j]:
            stack.append(Seq[j])
            break
        elif j == N-1:
            stack.append(-1)

print( " ".join(map(str, stack + [-1])))
