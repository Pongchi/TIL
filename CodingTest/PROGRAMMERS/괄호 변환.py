# 문제 주소 : https://programmers.co.kr/learn/courses/30/lessons/60058

def solution(p):
    if p == "":
        return ""
    
    lP, rP = 0, 0
    for bracket in p:
        if bracket == '(':
            lP += 1
        else:
            rP += 1

        if lP == rP:
            break
    
    u, v = p[:lP+rP], p[lP+rP:]
    if correct_check(u):
        return u + solution(v)
    else:
        return "(" + solution(v) + ")" + "".join([ '(' if bracket == ')' else ')' for bracket in u[1:-1] ])

def correct_check(p):
    stack = []
    for bracket in p:
        if bracket == '(':
            stack.append('(')
        else:
            if stack:
                stack.pop()
            else:
                return False
                
    return True if not stack else False


print( solution("()))((()") )