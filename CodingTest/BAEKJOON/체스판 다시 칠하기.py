import sys

# 기본 입력
N, M = map(int, sys.stdin.readline().split())
board = []
result = []
for n in range(N):
    board.append(sys.stdin.readline().rstrip())

for i in range(N-7):
    for j in range(M-7):
        ans1, ans2 = 0, 0
        for k in range(i, i+8):
            for l in range(j, j+8):
                if (k+l) % 2 == 0:
                    if board[k][l] != "W":
                        ans1 += 1
                    else:
                        ans2 += 1
                else:
                    if board[k][l] != "B":
                        ans1 += 1
                    else:
                        ans2 += 1

        result.append(ans1)
        result.append(ans2)

print( min(result) )