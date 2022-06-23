# 문제 주소 : https://www.acmicpc.net/problem/2343

N, M = map(int, input().split())
BlueRay = list(map(int, input().split()))
for i in range(1, N):
    BlueRay[i] += BlueRay[i-1]

left, right = 0, N-1
while left <= right:
    mid = (left+right) // 2
