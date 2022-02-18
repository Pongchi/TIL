# 문제 주소 : https://www.acmicpc.net/problem/2667

import sys

N = int(sys.stdin.readline())
MAP = [ sys.stdin.readline().rstrip() for i in range(N) ]
visited_apt = []
result = []

for i in range(len(MAP)):
    for j in range(len(MAP)):
        if (i, j) not in visited_apt:
            if MAP[i][j] == "1":
                stack = set([(i, j)])
                cnt = 0
                while stack:
                    apt = stack.pop()
                    cnt += 1
                    if apt not in visited_apt:
                        visited_apt.append(apt)
                        if apt[0] > 0 and MAP[apt[0]-1][apt[1]] == "1" and (apt[0]-1, apt[1]) not in visited_apt:
                            stack.add((apt[0]-1, apt[1]))
                        if apt[0] < N-1 and MAP[apt[0]+1][apt[1]] == "1" and (apt[0]+1, apt[1]) not in visited_apt:
                            stack.add((apt[0]+1, apt[1]))
                        if apt[1] > 0 and MAP[apt[0]][apt[1]-1] == "1" and (apt[0], apt[1]-1) not in visited_apt:
                            stack.add((apt[0], apt[1]-1))
                        if apt[1] < N-1 and MAP[apt[0]][apt[1]+1] == "1" and (apt[0], apt[1]+1) not in visited_apt:
                            stack.add((apt[0], apt[1]+1))

                result.append(cnt)
        else:
            visited_apt.append((i, j))

print( len(result) )
print( "\n".join(map(str, sorted(result))) )