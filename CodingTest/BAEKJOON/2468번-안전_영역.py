# 문제 주소 : https://www.acmicpc.net/problem/2468

def solution():
    vR = [1, -1, 0, 0]
    vC = [0, 0, 1, -1]
    def cntZone(N, MAP, level):
        answer = 0
        for i in range(len(MAP)):
            for j in range(len(MAP)):
                if MAP[i][j] > level:
                    answer += 1
                    stack = [(i, j)]
                    MAP[i][j] = 0
                    
                    while stack:
                        r, c = stack.pop()
                        
                        for k in range(4):
                            nR, nC = r + vR[k], c + vC[k]
                            if 0 <= nR < N and 0 <= nC < N and MAP[nR][nC] > level:
                                stack.append((nR, nC))
                                MAP[nR][nC] = 0

        return answer

    N = int(input())
    MAP = [ list(map(int, input().split())) for _ in range(N) ]

    _max = 1
    _min = 101
    for i in range(N):
        for j in range(N):
            if MAP[i][j] > _max:
                _max = MAP[i][j]
            if MAP[i][j] < _min:
                _min = MAP[i][j]
    
    result = 0
    for level in range(_min, _max+1):
        cnt = cntZone(N, [ MAP[i][:] for i in range(N) ], level)
        if result < cnt:
            result = cnt

    print(result if result else 1)

solution()