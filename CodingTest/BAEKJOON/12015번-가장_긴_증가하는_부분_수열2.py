# 문제 주소 : https://www.acmicpc.net/problem/12015

N = int(input())
A = list(map(int, input().split()))
stack = [A[0]]

for n in A[1:]:
    if stack[-1] < n:
        stack.append(n)

print( len(stack) )