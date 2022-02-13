import sys

N = int(sys.stdin.readline())
TOP = list(map(int, sys.stdin.readline().split()))
stack = []
result = [0] * N

for i in range(N):
    while stack and TOP[stack[-1]] < TOP[i]:
        stack.pop()

    result[i] = 0 if not stack else stack[-1]+1
    stack.append(i)

print( " ".join(map(str, result)) )
