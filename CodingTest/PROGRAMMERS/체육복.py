# 문제 주소 : https://programmers.co.kr/learn/courses/30/lessons/42862

def solution(n, lost, reserve):
    overlap = [i for i in lost if i in reserve]
    for i in overlap:
        lost.remove(i)
        reserve.remove(i)
    for i in lost:
        if i-1 in reserve: 
            reserve.remove(i-1)
            continue
        elif i+1 in reserve:
            reserve.remove(i+1)
            continue
        else:
            n -= 1
            continue

    return n