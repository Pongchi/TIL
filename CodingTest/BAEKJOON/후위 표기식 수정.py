Express = input()
stack = []
result = ''

for e in Express:
    if e.isalpha():
        result += e
    else:
        if e == '(' or not stack:
            stack.append(e)
        elif e == ')':
            while stack and stack[-1] != '(':
                result += stack.pop()
            stack.pop()

        elif e in ['*', '/']:
            while stack and stack[-1] in ['*', '/']:
                result += stack.pop()
            stack.append(e)
        
        elif e in ['+', '-']:
            while stack and stack[-1] in ['*', '/', ')']:
                result += stack.pop()
            stack.append(e)

while stack:
    result += stack.pop()

print( result )