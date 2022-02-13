import sys

N = int(sys.stdin.readline())
Seq = list(map(int, sys.stdin.readline().split()))
stack = []
answer = [0] * N

for i in range(N-1, -1, -1):
    while stack and stack[-1] <= Seq[i]:
        stack.pop()

    answer[i] = -1 if not stack else stack[-1]
    stack.append(Seq[i])
    
print(*answer)
