# 문제 주소 : https://programmers.co.kr/learn/courses/30/lessons/42862

def solution(n, lost, reserve):
    _reserve = list(set(reserve) - set(lost))
    _lost = list(set(lost) - set(reserve))
    for r in _reserve:
        if r-1 in _lost:
            _lost.remove(r-1)
        elif r+1 in _lost:
            _lost.remove(r+1)

    return n - len(_lost)