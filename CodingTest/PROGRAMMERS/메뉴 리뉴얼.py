# 문제 주소 : https://programmers.co.kr/learn/courses/30/lessons/72411

from itertools import combinations

def solution(orders, course):
    answer = []
    for a, b in combinations(orders, 2):
        intersection = set(a).intersection(set(b))
        if len(intersection) in course:
            answer.append("".join(sorted(intersection)))
            
    return sorted(set(answer))