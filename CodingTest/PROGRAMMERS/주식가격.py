# 문제 주소 : https://programmers.co.kr/learn/courses/30/lessons/42584

def solution(prices):
    answer = [0] * len(prices)
    stack = []
    
    for i in range(len(prices)):
        while stack and stack[-1][1] > prices[i]:
            idx, price = stack.pop()
            answer[idx] = i - idx
            
        stack.append((i, prices[i]))
    
    while stack:
        i, value = stack.pop()
        answer[i] = len(prices)-1 - i
        
    return answer