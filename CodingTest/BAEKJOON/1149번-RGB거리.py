# 문제 주소 : https://www.acmicpc.net/problem/1149

import sys

N = int(sys.stdin.readline())
# result = 0
# R, G, B = (0, 0, 0)
# before_select = ''

# for i in range(1, N+1):
#     r, g, b = map(int, sys.stdin.readline().split())
#     R, G, B = (R+r, G+g, B+b)
#     sort_RGB = sorted( (('R', R, r), ('G', G, g), ('B', B, b)), key=lambda x:x[1])

#     select = 0 if before_select != sort_RGB[0][0] else 1
#     result += sort_RGB[select][2]
#     before_select = sort_RGB[select][0]

# print( result )

RGB = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
for i in range(1, N):
    RGB[i][0] += min( RGB[i-1][1], RGB[i-1][2] )
    RGB[i][1] += min( RGB[i-1][0], RGB[i-1][2] )
    RGB[i][2] += min( RGB[i-1][0], RGB[i-1][1] )

print(min(RGB[-1]))