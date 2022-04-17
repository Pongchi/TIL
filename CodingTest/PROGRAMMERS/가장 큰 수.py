# 문제 주소 : https://programmers.co.kr/learn/courses/30/lessons/42746

def solution(numbers):
    return str(int("".join(sorted(map(str, numbers), reverse=True, key=lambda x : x*3))))