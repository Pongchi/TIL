# 문제 주소 : https://www.acmicpc.net/problem/2675

T = int(input())
result = []

for _ in range(T):
    R, S = input().split()
    R = int(R)
    s = ""
    for i in S:
        s += i*R
    
    result.append(s)
    
print( "\n".join(result) )

'''
T = int(input())
S = [ input().split() for i in range(T) ]

for s in S:
    print( "".join( [ i * int(s[0]) for i in s[1] ] ))
'''