def solution(board):
    def isSquare(dot, s):
        for i in range(1, s+1):
            if not (board[dot[0]][dot[1]+i] and board[dot[0]+i][dot[1]]):
                return False
        return board[dot[0]+s][dot[1]+s]

    max_s = 0
    S = (len(board), len(board[0]), (lambda x, y: x if x < y else y)(len(board), len(board[0])))
    for row in range(S[0]):
        for column in range(S[1]):
            if board[row][column] == 1:
                s = 1
                while (S[0] > row + s) and (S[1] > column + s):
                    if not isSquare((row, column), s):
                        break
                    s += 1
                    
                if s > max_s:
                    max_s = s
    
    return max_s ** 2

print( solution([[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]) )
