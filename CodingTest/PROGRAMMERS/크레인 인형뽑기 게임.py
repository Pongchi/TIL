# 문제주소 : https://programmers.co.kr/learn/courses/30/lessons/64061
# 전에 풀었지만 효율성 좋은 코드로 바꿈. ( because 코딩 스터디때 발표를 위해! )

def solution(board, moves):
    def pick_up(idx):
        for i in range(len(board)):
            if board[i][idx]:
                doll = board[i][idx]
                board[i][idx] = 0
                return doll
    
    answer = 0
    bucket = []
    for move in moves:
        if board[-1][move-1] == 0: continue;
        
        pickup_doll = pick_up(move-1)
        if bucket and bucket[-1] == pickup_doll:
            answer += 2
            bucket.pop()
        else:
            bucket.append( pickup_doll )
                          
    return answer