# 문제 주소 : https://programmers.co.kr/learn/courses/30/lessons/12905

def solution(board):
    for i in range(1, len(board)):
        for j in range(1, len(board[i])):
            if board[i][j]:
                board[i][j] = min(board[i-1][j-1], board[i-1][j], board[i][j-1]) + 1
    return max( [ max(board[i]) for i in range(len(board)) ] ) ** 2

print( solution([[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]) )