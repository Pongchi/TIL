# 문제 주소 : https://www.acmicpc.net/problem/1439

S = input()
arr = [S[0]]
cnt = [0, 0]

cnt[int(S[0])] += 1
for s in S[1:]:
    if arr[-1] != s:
        cnt[int(s)] += 1 
        arr.append(s)

print( min(cnt) if len(arr) > 1 else 0 )