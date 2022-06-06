# 문제 주소 : https://www.acmicpc.net/problem/1009

import sys

arr = [[10], [1], [6, 2, 4, 8], [1, 3, 9, 7], [6, 4], [5], [6], [1, 7, 9, 3], [6, 8, 4, 2], [1, 9]]
for _ in range(int(sys.stdin.readline())):
    a, b = map(int, sys.stdin.readline().split())

    if(a % 10) in [0, 1, 5, 6]:
        print(arr[a%10][0])
    
    elif (a % 10) in [4, 9]:
        print(arr[a%10][b%2])
    
    else:
        print(arr[a%10][b%4])