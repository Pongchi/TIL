import sys

def isGood(S):
    stack = []
    for s in S:
        if stack:
            if stack[-1] == s:
                stack.pop()
            else:
                stack.append(s)
        else:
            stack.append(s)

    return True if not stack else False

    
N = int(sys.stdin.readline())
result = 0

for i in range(N):
    if isGood(sys.stdin.readline().rstrip()):
        
        result += 1

print( result )
