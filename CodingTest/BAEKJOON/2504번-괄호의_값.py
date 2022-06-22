bracket = input()

def findValue(b):
    stack = []
    tmp = 1
    total = 0
    for i in range(len(b)):
        print(total)
        print(tmp, stack)
        if b[i] in ['(', '[']:
            stack.append(b[i])
            tmp *= 2 if b[i] == '(' else 3
        else:
            if not stack or ((stack[-1] == '(' and b[i] != ')') or (stack[-1] == '[' and b[i] != ']')):
                return 0
            else:
                if b[i-1] == '(' and b[i] == ')':
                    tmp += 2
                elif b[i-1] == '[' and b [i] == ']':
                    tmp += 3
                else:
                    tmp //= 2 if b[i] == ')' else 3
                    total += tmp

                stack.pop()
                if not stack:
                    tmp = 1
    return total if not stack else 0

print( findValue(bracket) )
