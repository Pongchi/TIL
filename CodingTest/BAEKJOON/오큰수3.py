import sys

N = int(sys.stdin.readline())
Seq = tuple( map(int, sys.stdin.readline().split()) )
stack = []

def isBigger(Seq):
    while len(stack) != len(Seq)-1:
        for num in Seq[len(stack)+1:]:
            for idx in range(len(stack), N):
                if Seq[idx] < num:
                    stack.append(num)
                    break
    return " ".join(map(str, stack + [-1] ))

print( isBigger(Seq) )
