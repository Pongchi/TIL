N = int(input())
stack = [1, 2, 2]

while len(stack) < N:
    stack.append( 2 if len(stack) <= stack[-1] else stack[-1] + 2)
    
print(stack[N-1])
