# 문제 주소 : https://www.acmicpc.net/problem/11478

S = input()
SET = set()

for i in range(len(S)):
    for j in range(i, len(S)):
        SET.add( S[i:j+1] )

print( len(SET) )