def isEnd(N):
    stack = []
    for n in str(N):
        if len(stack) >= 3:
            return True
        if n == '6':
            stack.append(n)
        else:
            stack.clear()
    return True if len(stack) >= 3 else False

N = int(input())
n = 665
idx = 0

while N != idx:
    n += 1
    if isEnd(n):
        idx += 1
        print(n)
        
print(n)
