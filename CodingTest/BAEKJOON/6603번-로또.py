# 문제 주소 : https://www.acmicpc.net/problem/6603

def combination(arr):
    result = []
    def recur(i):
        if len(result) == 6:
            print(*result)
            return

        for j in range(i, len(arr)):
            result.append(arr[j])
            recur(j+1)
            result.pop()

    return recur(0)

while True:
    arr = list(map(int, input().split()))
    if arr[0] == 0:
        break
    
    combination(arr[1:])
    print()