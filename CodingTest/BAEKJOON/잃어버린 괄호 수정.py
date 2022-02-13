Exp = input()

stack = [Exp[0]]
B = False
for e in Exp[1:]:
    if e.isdigit():
        if stack[-1] == "+" or stack[-1] == "-") and e == "0":
            continue
        stack.append(e)
    else:
        if e == "+":
            stack.append(e)
        else:
            if B:
                stack.extend([")", e, "("])
            else:
                B = True
                stack.extend([e, "("])

if B:
    stack.append(")")
print( eval("".join(stack)) )