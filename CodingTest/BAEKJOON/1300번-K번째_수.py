# 문제 주소 : https://www.acmicpc.net/problem/1300

N = int(input())
k = int(input())

i = k // N
j = k % N

print( (i+1) * (j+1) )