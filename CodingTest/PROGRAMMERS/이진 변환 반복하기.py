# 문제 주소 : https://programmers.co.kr/learn/courses/30/lessons/70129

def solution(s):
    cnt_zero, cnt = 0, 0
    
    while s != '1':
        tmp = ''
        cnt += 1
        
        for i in s:
            if i != '0':
                tmp += i
            else:
                cnt_zero += 1
        s = bin(len(tmp))[2:]
                               
    return [cnt, cnt_zero]