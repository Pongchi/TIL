# 문제 주소 : https://www.acmicpc.net/problem/1032

N = int(input())
cmds = [ input() for _ in range(N) ]

result = ''
for i in range(len(cmds[0])):
    for cmd in cmds[1:]:
        if cmd[i] != cmds[0][i]:
            result += '?'
            break
    else:
        result += cmds[0][i]

print( result )