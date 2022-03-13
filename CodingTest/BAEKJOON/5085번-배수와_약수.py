# 문제 주소 : https://www.acmicpc.net/problem/5086
import sys

while True:
    a, b  = map(int, sys.stdin.readline().split())
    if a == b == 0:
        break

    print("factor" if b % a == 0 else ("multiple" if a % b == 0 else "neither"))