# 문제 주소 : https://www.acmicpc.net/problem/1992

N = int(input())
MAP = [ list(input()) for i in range(N) ]
result = []

def QuadTree(N, x, y):
    color = MAP[x][y]
    
    for row in range(x, x+N):
        for col in range(y, y+N):
            if color != MAP[row][col]:
                result.append('(')
                QuadTree(N//2, x, y)
                QuadTree(N//2, x, y+N//2)
                QuadTree(N//2, x+N//2, y)
                QuadTree(N//2, x+N//2, y+N//2)
                result.append(')')
                return

    result.append(color)

QuadTree(N, 0, 0)
print( "".join(result) )