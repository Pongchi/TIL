# 문제 주소 : https://www.acmicpc.net/problem/5543

burgers = [ int(input()) for _ in range(3) ]
drinks = [ int(input()) for _ in range(2) ]

print( min(burgers) + min(drinks) - 50 )