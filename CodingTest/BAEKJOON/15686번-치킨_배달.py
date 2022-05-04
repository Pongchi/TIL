# 문제 주소 : https://www.acmicpc.net/problem/15686

import sys
from queue import deque

N, M = map(int, sys.stdin.readline().split())
MAP = [ list(map(int, sys.stdin.readline().split())) for _ in range(N) ]