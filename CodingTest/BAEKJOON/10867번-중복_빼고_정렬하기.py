# 문제 주소 : https://www.acmicpc.net/problem/10867

N = int(input())
print(*sorted(set(map(int, input().split()))))