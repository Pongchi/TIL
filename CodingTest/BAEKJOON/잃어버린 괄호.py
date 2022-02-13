Exp = input()

result = ""
tmp = ""
stack = []
B = False
for e in Exp:
    if e.isdigit():
        stack.append(e)
    else:
        tmp = "".join(stack)
        stack.clear()
        if e == "+":              
            result += str(int(tmp)) + e
        else:
            if B:
                result += str(int(tmp)) + ")" + e + "("
            else:
                result += str(int(tmp)) + e + "("
                B = True

result += str(int("".join(stack))) + ")" if B else str(int("".join(stack)))
print( eval(result) )