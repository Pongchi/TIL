# 문제 주소 : https://programmers.co.kr/learn/courses/30/lessons/12913
# 문재 풀이 : 전형적인 DP 문제라고 생각했고, 내려오면서 column 이 같은 것을 뺴고 가장 큰값을 더하면서 내려옴.

def solution(land):
    h, w = len(land), len(land[0])
    for row in range(1, h):
        for col in range(w):
            land[row][col] += max([ land[row-1][i] for i in range(w) if i != col])
    
    return max(land[-1])