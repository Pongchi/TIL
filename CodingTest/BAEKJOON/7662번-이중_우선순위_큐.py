# 문제 주소 : https://www.acmicpc.net/problem/7662

import sys

for T in range(int(sys.stdin.readline())):
    queue = []
    for k in range(int(sys.stdin.readline())):
        cmd, value = sys.stdin.readline().split()
        value = int(value)

        if cmd == "I":
            queue.append(value)
    
        else:
            queue.sort()