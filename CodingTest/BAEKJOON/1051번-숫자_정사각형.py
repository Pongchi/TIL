# 문제 주소 : https://www.acmicpc.net/problem/1051

N, M = map(int, input().split())
MAP = [ list(map(int, input())) for _ in range(N) ]

def find_max_square(n):
    if n == 1:
        return 1

    for row in range(N-n+1):
        for i in range(M-n+1):
            if MAP[row][i] == MAP[row][i+n-1] == MAP[row+n-1][i] == MAP[row+n-1][i+n-1]:
                return n**2

    return find_max_square(n-1)

print(find_max_square(N))