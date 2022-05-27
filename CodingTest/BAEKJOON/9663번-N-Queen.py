# 문제 주소 : https://www.acmicpc.net/problem/9663
# cheatsheet = [1, 0, 0, 2, 10, 4, 40, 92, 352, 724, 2680, 14200, 73712, 365596]

def pprint(MAP):
    for i in range(len(MAP)):
        print(*MAP[i])

def N_Queen(N):
    MAP = [ [0]*N for _ in range(N) ]
    result = 0
    def fill(x, y, v):
        for i in range(N):
            MAP[x][i] += v
        for i in range(0, N):
            MAP[i][y] += v
        for i in range(N+1):
            if 0 <= x-i and 0 <= y-i:
                MAP[x-i][y-i] += v
            if 0 <= x-i and y+i < N:
                MAP[x-i][y+i] += v
            if x+i < N and y+i < N:
                MAP[x+i][y+i] += v
            if x+i < N and 0 <= y-i:
                MAP[x+i][y-i] += v

    def recur(x):
        nonlocal result
        for i in range(N):
            if MAP[x][i] == 0:
                if x == N-1:
                    result += 1
                    return

                fill(x, i, 1)
                recur(x+1)
                fill(x, i, -1)

    recur(0)
    return result

print( N_Queen(int(input())) )