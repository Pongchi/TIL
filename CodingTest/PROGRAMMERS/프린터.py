# 문제 주소 : https://programmers.co.kr/learn/courses/30/lessons/42587

def solution(priorities, location):
    answer = 0
    priority = sorted(priorities)
    priorities = [ (i,p) for i, p in enumerate(priorities) ]
    
    while priorities:
        i, p = priorities.pop(0)
        
        if p == priority[-1]:
            answer += 1
            priority.pop()
            if i == location:
                return answer
        else:
            priorities.append((i, p))
                