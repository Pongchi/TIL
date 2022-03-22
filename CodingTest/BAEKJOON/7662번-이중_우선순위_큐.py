# 문제 주소 : https://www.acmicpc.net/problem/7662

import sys

for T in range(int(sys.stdin.readline())):
    print("========================")
    queue = []
    for k in range(int(sys.stdin.readline())):
        cmd, value = sys.stdin.readline().split()
        value = int(value)

        if cmd == "I":
            queue.append(value)
    
        else:
            if queue:
                idx = 0
                if value == 1:
                    for i in range(len(queue)):
                        if queue[idx] < queue[i]:
                            idx = i
                else:
                    for i in range(len(queue)):
                        if queue[idx] > queue[i]:
                            idx = i
                queue.pop(idx)
    
    _max, _min = 0, 1000001
    for i in range(len(queue)):
        if queue[i] < _min:
            _min = queue[i]
        if queue[i] > _max:
            _max = queue[i]

    if queue:
        print(_max, _min)
    else:
        print("EMPTY")