# 문제 주소 : https://programmers.co.kr/learn/courses/30/lessons/68645

def solution(n):
    answer = [ [0]*(i+1) for i in range(n) ]
    
    def recur(n, i, row, col):
        if n < 1:
            return
        elif n == 1:
            answer[row][col] = i
        else:
            for j in range(n-1):
                answer[row+j][col] = i
                i += 1
            for j in range(n-1):
                answer[row+n-1][col+j] = i
                i += 1
            for j in range(n-1):
                answer[row+n-1-j][col+n-1-j] = i
                i += 1
            
        recur(n-3, i, row+2, col+1)
            
    recur(n, 1, 0, 0)
    return sum(answer, [])