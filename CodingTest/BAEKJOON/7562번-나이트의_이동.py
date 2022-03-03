# 문제 주소 : https://www.acmicpc.net/problem/7562

import sys
from queue import deque

vector_row = [2, 2, 1, 1, -1, -1, -2, -2]
vector_col = [1, -1, 2, -2, 2, -2, 1, -1]
def bfs(L, c, d):
    queue = deque([c])
    visited = {c:0}
    
    while queue:
        l = queue.popleft()
        cnt = visited[l]
        if l == d:
            return cnt

        for i in range(8):
            moved_loc = (l[0]+vector_row[i], l[1]+vector_col[i])
            if all((0 <= moved_loc[0], moved_loc[1] <= L-1)) and moved_loc not in visited:
                visited[moved_loc] = cnt+1
                queue.append(moved_loc)

for T in range(int(sys.stdin.readline())):
    L = int(sys.stdin.readline())
    current_Location = tuple(map(int, sys.stdin.readline().split()))
    dst_Location = tuple(map(int, sys.stdin.readline().split()))

    print(bfs(L, current_Location, dst_Location))