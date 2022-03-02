# 문제 주소 : https://www.acmicpc.net/problem/11723

import sys

SET = set()
for _ in range(int(sys.stdin.readline())):
    cmd = sys.stdin.readline().split()
    if cmd[0] == "add":
        SET.add(cmd[1])
    
    elif cmd[0] == "check":
        print(1 if cmd[1] in SET else 0)
    
    elif cmd[0] == "remove":
        SET.discard(cmd[1])

    elif cmd[0] == "toggle":
        if cmd[1] in SET:
            SET.remove(cmd[1])
        else:
            SET.add(cmd[1])
    
    elif cmd[0] == "all":
        SET = set([i for i in range(1, 21)])
    
    else:
        SET.clear()