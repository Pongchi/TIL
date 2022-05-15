# 문제 주소 : https://www.acmicpc.net/problem/2908

A, B = input().split()
A, B = int(A[::-1]), int(B[::-1])

print( A if A > B else B )