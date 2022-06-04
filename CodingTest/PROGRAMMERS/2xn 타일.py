# 문제 주소 : https://programmers.co.kr/learn/courses/30/lessons/12900

def solution(n):
    a, b = 1, 2
    for i in range(n-1):
        a, b = b, a+b
    
    return a % 1000000007