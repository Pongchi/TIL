# 문제 주소 : https://www.acmicpc.net/problem/11053

N = int(input())
A = list(map(int, input().split()))

def LIS():
    Di = [0]
    X = [0]
    D = [0]

    for i in range(N):
        if X[-1] < A[i]:
            X.append(A[i])
            Di.append(D[-1]+1)

        else:
            for j in range(len(Di)):
                if Di[j] < A[i]:
                    X[j-1] = A[i]
                    break 

    return len(Di)

print( LIS() - 1)