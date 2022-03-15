# 문제 : 이것이 코딩테스트다 책의 DFS/BFS 에 있는 문제.
# 14분 컷!

import sys
from queue import deque

N, M = map(int, sys.stdin.readline().split())
Board = [ list(map(int, sys.stdin.readline().rstrip())) for i in range(N) ]
vectorR = [1, -1, 0, 0]
vectorC = [0, 0, 1, -1]

result = 0 
for row in range(N):
    for column in range(M):
        if Board[row][column] == 0:
            queue = deque([(row, column)])
            result += 1

            while queue:
                r,c = queue.popleft()
                Board[r][c] = 1

                for i in range(4):
                    vR = r+vectorR[i]
                    vC = c+vectorC[i]
                    if 0 <= vR < N and 0 <= vC < M and Board[vR][vC] == 0:
                        queue.append((vR, vC))

print( result )