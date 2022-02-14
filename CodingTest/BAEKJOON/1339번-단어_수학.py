# 문제 주소 : https://www.acmicpc.net/problem/1339

import sys

N = int(sys.stdin.readline())
words = sorted([ sys.stdin.readline().rstrip() for i in range(N) ], key=lambda x : len(x))
word_value = {}
stack = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
result = [""] * len(words)

for i in range(len(max(words, key=lambda x : len(x))), 0, -1):
    for idx, word in enumerate(words):
        if not len(word) >= i:
            continue
        
        if not word_value.get(word[-i], 0):
            word_value[word[-i]] = stack.pop()
        result[idx] += word_value[word[-i]]

print( sum(map(int, result)) )