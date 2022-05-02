# 문제 주소 : https://www.acmicpc.net/problem/1744

N = int(input())
arr = []
zero, result = 0, 0
for _ in range(N):
    n = int(input())
    if n != 0:
        arr.append(n)
    else:
        zero += 1

arr.sort()
while zero:
    if arr[0] < 0:
        arr.pop(0)
    else:
        break

while len(arr) > 1:
    if arr[-1] > 0:
        a, b = arr.pop(), arr.pop()
    else:
        a, b = arr.pop(0), arr.pop(0)

    if not (a == 1 and b == 1) and (a > 0 and b > 0) or (a < 0 and b < 0):
        result += a*b

    else:
        result += a+b

print( result + (arr[0] if arr else 0))