# 문제 주소 : https://www.acmicpc.net/problem/11722

# 문제 주소 : https://www.acmicpc.net/problem/11053

N = int(input())
A = list(map(int, input().split()))

dp = [A[0]]
for i in range(1, N):
    if dp[-1] > A[i]:
        dp.append(A[i])
    
    else:
        for j in range(len(dp)):
            if dp[j] <= A[i]:
                dp[j] = A[i]
                break

print( len(dp) )