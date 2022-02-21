# 문제 주소 : https://programmers.co.kr/learn/courses/30/lessons/42885?language=python3

def solution(people, limit):
    people.sort()
    result = 0
    idx = 0

    while people and idx < len(people):
        if len(people) == 1:
            result += 1
            people.pop()
        
        elif people[idx] + people.pop() <= limit:
            result += 1
            idx += 1
        else:
            result += 1

    return result



print( solution([70, 50, 80, 50], 100) )
print( solution([70, 80, 50], 100) )