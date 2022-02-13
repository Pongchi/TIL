
import sys

"""
N, K = list(map(int, sys.stdin.readline().split()))
Coins = [int(sys.stdin.readline()) for i in range(N)]

result = 0
for c in Coins[::-1]:
    while K >= c:
        K -= c
        result += 1

    if K == 0:
        break

print( result )
"""

N, K = list(map(int, sys.stdin.readline().split()))
Coins = [int(sys.stdin.readline()) for i in range(N)]

result = 0
for coin in Coins[::-1]:
    if K >= coin:
        result, K = (result + K//coin, K%coin)
    
    if K == 0:
        break

print( result )