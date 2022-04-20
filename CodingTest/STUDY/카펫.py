# 문제 주소 : https://programmers.co.kr/learn/courses/30/lessons/42842

def get_divisor(n):
    return [ (n//i, i) for i in range(1, int(n**0.5)+1) ]

def solution(brown, yellow):
    for w, h in get_divisor(yellow):
        if w*2 + h*2 + 4 == brown:
            return [w+2, h+2]