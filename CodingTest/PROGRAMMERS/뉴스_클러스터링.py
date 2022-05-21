# 문제 주소 : https://programmers.co.kr/learn/courses/30/lessons/17677

def toSET(S):
    result = set()
    for i in range(len(S)-1):
        s = S[i:i+2]
        if s.isalpha():
            result.add(s)
    return result 

def solution(str1, str2):
    set1 = toSET(str1.upper())
    set2 = toSET(str2.upper())
    
    a, b = len(set1 & set2), len(set1 | set2)
    result = a / b if b != 0 else 1
    return  int(result * 65536)