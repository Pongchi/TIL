# 문제 주소 : https://www.acmicpc.net/problem/1016

_min, _max = map(int, input().split())
NoNos = [False]+ [True] * (_max)

for i in range(2, int(_max**0.5)+1):
    multi = i*i
    j = 1
    while multi*j <= _max:
        NoNos[multi*j] = False
        j += 1
        
print( sum(NoNos[_min:]) )