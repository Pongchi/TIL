import sys

def isFLD(left, right):
    for i in right:
        if left.pop() != i:
            return "no"
    return "yes"
            
while True:
    N = sys.stdin.readline().rstrip()
    if N == "0":
        break
        
    L = len(N)
    left = list(N[:L//2])
    right = N[L//2:] if L % 2 == 0 else N[L//2+1:]
    print( isFLD(left, right) )
