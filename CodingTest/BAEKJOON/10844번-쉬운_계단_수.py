# 문제 주소 : https://www.acmicpc.net/problem/10844

N = int(input())

stair_number = { i:[] for i in range(1, N+1) }
stair_number[1] = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

for i in range(2, N+1):
    for n in stair_number[i-1]:
        if int(n[-1])-1 >= 0:
            stair_number[i].append(n+str(int(n)-1))
        if int(n[-1])+1 <= 9:
            stair_number[i].append(n+str(int(n)+1))

print(len(stair_number[N]))