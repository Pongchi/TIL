import sys

S = list(sys.stdin.readline().rstrip())
cursor = len(S)

for i in range(int(sys.stdin.readline())):

    cmd = sys.stdin.readline().split()
    if cmd[0] == 'P':
        S.insert(cursor, cmd[1])
        cursor += 1
    elif cmd[0] == 'L':
        if cursor > 0:
            cursor -= 1
    elif cmd[0] == 'D':
        if cursor < len(S):
            cursor += 1
    else: # cmd[0] == 'B'
        if cursor > 0:
            S.pop(cursor-1)
            cursor -= 1
print("".join(S))
