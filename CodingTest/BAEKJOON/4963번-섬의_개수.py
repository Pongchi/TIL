# 문제 주소 : https://www.acmicpc.net/problem/4963

from queue import deque

vr = [1, -1, 0, 0, -1, -1, 1, 1]
vc = [0, 0, 1, -1, -1, 1, -1, 1]

result = []
while True:
    w, h = map(int, input().split())
    if w == h == 0:
        break
    
    answer = 0
    MAP = [ list(map(int, input().split())) for _ in range(h) ]

    for i in range(h):
        for j in range(w):
            if MAP[i][j]:
                MAP[i][j] = 0
                answer += 1
                queue = deque([(i, j)])

                while queue:
                    r, c = queue.popleft()
                    
                    for k in range(8):
                        dr, dc = vr[k] + r, vc[k] + c

                        if 0 <= dr < h and 0 <= dc < w and MAP[dr][dc]:
                            queue.append((dr, dc))
                            MAP[dr][dc] = 0

    print(answer)