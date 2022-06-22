# 문제 주소 : https://www.acmicpc.net/problem/17413

S = input()
stack = []
arrow = False
result = ''

for s in S:
    if s == '>':
        arrow = False
        result += s

    elif arrow:
        result += s
    
    elif s == '<':
        while stack:
            result += stack.pop()
        arrow = True
        result += s
    
    elif s == ' ':
        result += s
    else:
        stack.append(s)

while stack:
    result += stack.pop()

print(result)