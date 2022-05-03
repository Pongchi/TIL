# 문제 주소 : https://www.acmicpc.net/problem/1912

N = int(input())
arr = list(map(int, input().split()))
dp = [arr[0]]

for i in range(1, N):
    dp.append( max(dp[-1]+arr[i], arr[i]) )

print(max(dp))