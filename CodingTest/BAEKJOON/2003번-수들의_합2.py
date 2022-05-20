# 문제 주소 : https://www.acmicpc.net/problem/2003

N, M = map(int, input().split())
arr = list(map(int, input().split()))
dp = [arr[0]]
result = 0

for i in arr[1:]:
    dp.append( dp[-1] + i if dp[-1] < M else dp[-1])
    if dp[-1] == M:
        result += 1

print( result )
print(dp)