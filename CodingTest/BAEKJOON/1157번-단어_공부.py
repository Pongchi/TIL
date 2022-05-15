# 문제 주소 : https://www.acmicpc.net/problem/1157

S = input().upper()
word = { i:0 for i in 'ABCDEFGHIJKLNMOPQRSTUVWXYZ' }

for i in S:
	word[i] += 1

word = sorted(word.items(), key=lambda x:x[1], reverse=True)
print( word[0][0] if word[0][1] != word[1][1] else '?' )