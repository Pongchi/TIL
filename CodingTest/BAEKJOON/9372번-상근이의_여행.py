# 문제 주소 : https://www.acmicpc.net/problem/9372

for T in range(int(input())):
    N, M = map(int, input().split())
    graph = [ [] for _ in range(N) ]