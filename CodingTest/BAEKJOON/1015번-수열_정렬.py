# 문제 주소 : https://www.acmicpc.net/problem/1015

N = int(input())
arr = list(enumerate(map(int, input().split())))
A = { x[0]:(i, x[1]) for i, x in enumerate(sorted(arr, key=lambda x : x[1])) }

print(*[ A[i][0] for i, v in arr ])