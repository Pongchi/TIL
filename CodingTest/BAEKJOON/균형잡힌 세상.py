import sys

def isBalance(S):
    stack = []
    for s in S:
        if s == "(" or s == "[":
            stack.append(s)
        elif s == ")":
            if not len(stack):
                return "no"
            elif stack.pop() != "(":
                return "no"
        elif s == "]":
            if not len(stack):
                return "no"
            elif stack.pop() != "[":
                return "no"

    return "yes" if not len(stack) else "no"

while True:
    S = sys.stdin.readline().rstrip()
    if S == ".":
        break
    print( isBalance(S) )
