# 문제 주소 : https://www.acmicpc.net/problem/1939

import sys

N, M = map(int, sys.stdin.readline().split())
MAP = [[0] * N] * N
for m in range(M):
    A, B, C = map(int, sys.stdin.readline().split())
    
START, END = map(int, sys.stdin.readline().split())