# 문제 주소 : https://www.acmicpc.net/problem/3034

import sys

N, W, H = map(int, sys.stdin.readline().split())
hypotenuse = (W*W + H*H) ** 0.5


for _ in range(N):
    print( "DA" if float(sys.stdin.readline()) <= hypotenuse else "NE" )