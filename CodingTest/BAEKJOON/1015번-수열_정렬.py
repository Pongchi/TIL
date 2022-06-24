# 문제 주소 : https://www.acmicpc.net/problem/1015

N = int(input())
arr = list(map(int, input().split()))
A = sorted(enumerate(sorted(arr)), key=lambda x : x[0])

print(*[ A[i-1][0] for i in arr])