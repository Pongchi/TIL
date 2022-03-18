# 문제 주소 : https://www.acmicpc.net/problem/16234

from queue import deque

N, L, R = map(int, input().split())
MAP = [ list(map(int, input().split())) for n in range(N) ]
vectorR = [1, -1, 0, 0]
vectorC = [0, 0, 1, -1]

queue = deque([])

def find_organzation():
    return []

while queue:
    pass