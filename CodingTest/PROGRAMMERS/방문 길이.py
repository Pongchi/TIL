# 문제 주소 : https://programmers.co.kr/learn/courses/30/lessons/49994

def solution(dirs):
    answer = 0
    MAP = [ [0] * 11 for _ in range(11) ]
    x, y = 5, 5
    for dir in dirs:
        if MAP[x][y] == 0:
            answer += 1
            MAP[x][y] = 1
        
        if dir == "U":
            x += 1 if x < 10 else 0
        elif dir == 'D':
            x -= 1 if 0 < x else 0
        elif dir == 'L':
            y -= 1 if 0 < y else 0
        else:
            y += 1 if y < 10 else 0
            
            
    return answer