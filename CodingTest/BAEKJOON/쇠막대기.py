pipe = input()
stack = []
total = 0
for p in range(len(pipe)):
    print(total, stack)
    if pipe[p] == '(':
        stack.append('(')
    else:
        stack.pop()
        if pipe[p-1] == '(':
            total += len(stack)
        else:
            total += 1
            
print( total )
