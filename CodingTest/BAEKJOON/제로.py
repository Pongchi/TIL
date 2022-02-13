import sys

K = int(sys.stdin.readline())
stack = []
result = 0

for _ in range(K):
    ipt = int(sys.stdin.readline())
    if ipt != 0:
        stack.append(ipt)
        result += ipt
    else:
        result -= stack[-1]
        stack.pop()
        
print( result )
