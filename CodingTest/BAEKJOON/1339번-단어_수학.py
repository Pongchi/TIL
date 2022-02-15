# 문제 주소 : https://www.acmicpc.net/problem/1339
# 문제 풀이 : 각 알파벳의 자리수 값을 다 더해놨다가 큰 값부터 차례대로 weight를 곱함. ( 10의 자리에 있다면 10, 100의 자리에 있다면 100을 각 알파벳에 더함.)
# 소요 시간 : 1일..

import sys

N = int(sys.stdin.readline())
words = [ sys.stdin.readline().rstrip() for i in range(N) ]
ans = [0] * 26
weight = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for word in words:
    for i, w in enumerate(word):
        ans[ord(w)-65] += 10 ** (len(word)-i-1)


print( sum(map(lambda x : x * weight.pop() if x != 0 else 0 , sorted(ans, reverse=True))) )