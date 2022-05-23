# 문제 주소 : https://www.acmicpc.net/problem/2470

N = int(input())
arr = sorted(map(int, input().split()))
result = [arr[0], arr[1]] # [ A, B] = { A < B }
left, right = 0, N-1

while left < right:
    S = arr[right]+arr[left]
    
    if abs(S) <= abs(result[0]+result[1]):
        result = [ arr[left], arr[right] ]
        left += 1
        if S == 0:
            break
    else:
        right -= 1

print(*result)