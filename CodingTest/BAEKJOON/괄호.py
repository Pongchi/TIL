import sys

def isVPS(s):
    while s:
        print(s)
        if len(s) >= 2:
            if s[-1] == ")":
                for i in reversed(range(len(s)-1)):
                    if s[i] == "(":
                        del s[i], s[-1]
                        break
                    elif i == 0:
                        return print("NO")
            else:
                return print("NO")
        else:
            return print("NO")
    return print("YES")

T = int(sys.stdin.readline())
Datas = [ isVPS(list(sys.stdin.readline()[:-1])) for i in range(T) ]
