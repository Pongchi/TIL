# 문제 주소 : https://www.acmicpc.net/problem/1072

X, Y = map(int, input().split())
rate = int(Y/X*100)

if X == Y:
    print(-1)

else:
    left, right = 1, 1000000000
    
    while left <= right:
        middle = (left+right) // 2
        if rate >= int((Y+middle) / (X+middle) * 100):
            left = middle + 1
        else:
            right = middle - 1

    print(left)