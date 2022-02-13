Express = input()
stack = []
result = ""

for e in Express:
    # 피연산자는 그대로 출력
    if e.isalpha():
        result += e

    # 연산자 일 경우
    else:
        # 스택이 비어있다면 자신을 바로 추가
        if not stack or e == '(':
            stack.append(e)
        else:
            # stack의 top이 자신보다 우선순위가 낮은 연산자를 만날 때까지 pop하고 자신을 담음.
            if e == ')':
                while stack and stack[-1] != '(':
                    result += stack.pop()
                stack.pop()
            elif e in ['*', '/']:
                if stack[-1] in ['*', '/']:
                    result += stack.pop()
                else:
                    while stack and stack[-1] not in ['+', '-']:
                        result += stack.pop()
                stack.append(e)

            else:
                while stack and stack[-1] not in ['+', '-']:
                    result += stack.pop()
                stack.append(e)

for i in stack:
    result += i

print( result )