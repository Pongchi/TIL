# 문제 주소 : https://www.acmicpc.net/problem/2167

N, M = map(int, input().split())
MAP = [ list(map(int, input().split())) for _ in range(N) ]

for i in range(N):
    for j in range(1, M):
        MAP[i][j] += MAP[i][j-1]

for K in range(int(input())):
    x1, y1, x2, y2 = map(lambda x : int(x)-1, input().split())
    result = 0
    for i in range(x1, x2+1):
        result += MAP[i][y2] - (MAP[i][y1-1] if y1 != 0 else 0)

    print(result)