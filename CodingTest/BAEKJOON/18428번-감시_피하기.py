# 문제 주소 : https://www.acmicpc.net/problem/18428

N = int(input())
MAP = [ input().split() for i in range(N) ]
teachers = [ (x, y) for x in range(N) for y in range(N) if MAP[x][y] == "T" ]
result = False

def bypass_watch():
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    for loc in teachers:
        for i in range(4):
            idx = 0
            while True:
                idx += 1
                x = loc[0] + dx[i] * idx
                y = loc[1] + dy[i] * idx
                if not (0 <= x < N and 0 <= y < N):
                    break
                
                if MAP[x][y] == "S":
                    return False
                elif MAP[x][y] in ["O", "T"]:
                    break
    
    return True

def back_search(walls):
    global result
    if result or walls == 3:
        if bypass_watch():
            result = True
        return 

    for i in range(N):
        for j in range(N):
            if MAP[i][j] == "X":
                MAP[i][j] = "O"
                back_search(walls+1)
                MAP[i][j] = "X"

back_search(0)
print("YES" if result else "NO")