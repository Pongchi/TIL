# 문제 주소 : https://programmers.co.kr/learn/courses/30/lessons/68936

def solution(arr):
    answer = [0, 0]
    def QuadTree(N, x, y):
        color = arr[x][y]
        for row in range(x, x+N):
            for col in range(y, y+N):
                if arr[row][col] != color:
                    QuadTree(N//2, x, y)
                    QuadTree(N//2, x, y+N//2)
                    QuadTree(N//2, x+N//2, y)
                    QuadTree(N//2, x+N//2, y+N//2)
                    return
                
        answer[int(color)] += 1
                    
    QuadTree(len(arr), 0, 0)      
    return answer

print( solution([[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]])) # [4, 9]