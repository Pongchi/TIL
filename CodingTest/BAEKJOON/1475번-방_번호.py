# 문제 주소 : https://www.acmicpc.net/problem/1475

from math import ceil

N = input()
arr = [0] * 10
result = 0

for n in N:
    arr[int(n)] += 1

arr[6] += arr[9]
arr.pop()

for i in range(9):
    if arr[i] > result:
        result = arr[i] if i != 6 else ceil(arr[i]/2)

print(result)