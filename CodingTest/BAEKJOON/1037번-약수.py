# 문제 주소 : https://www.acmicpc.net/problem/1037

N = int(input())
lst = sorted(map(int, input().split()))

print( lst[0] * lst[-1] if len(lst) >= 2 else lst[0] ** 2 )