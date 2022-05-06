# 문제 주소 : https://programmers.co.kr/learn/courses/30/lessons/76502

def isValid(s):
    stack = []
    for word in s:
        if word in ['[', '(', '{']:
            stack.append(word)
        else:
            if stack:
                p = stack.pop()
                if (p == '(' and word != ')') or (p == '[' and word != ']') or (p == '{' and word != '}'):
                    return False
            else:
                return False
            
    return True if not stack else False

def solution(s):
    result = 0
    for i in range(len(s)):
        if isValid(s[i:] + s[:i]):
            result += 1
            
    return result