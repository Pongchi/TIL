# 문제 주소 : https://www.acmicpc.net/problem/2525

H, M = map(int, input().split())
C = int(input()) 

M += C % 60
if M >= 60:
    H += 1
M %= 60

H += C // 60
H %= 24

print(H, M)