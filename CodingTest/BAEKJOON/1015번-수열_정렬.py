# 문제 주소 : https://www.acmicpc.net/problem/1015

N = int(input())
arr = list(map(int, input().split()))
A = { v:i for i, v in enumerate(sorted(arr)) }

print(*[ A[i] for i in arr])