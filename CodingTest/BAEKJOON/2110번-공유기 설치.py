# 문제 주소 : https://www.acmicpc.net/problem/2110
# 문제 분류 : 이분 탐색, 매개 변수 탐색
# 문제 풀이 : 정렬 후, 최소 길이를 정해주면 그 최소 길이 이상의 위치에 공유기를 설치한다. 그래서 그 갯수를 반환하는 한다.
#            그 갯수에 따라 이분탐색법으로 계속 탐색함.
# 소요 시간 : 약 25분

import sys

N, C = map(int, sys.stdin.readline().split())
Location = sorted([ int(sys.stdin.readline()) for i in range(N) ])
Start = 1
End = Location[-1]

def placeModem(min_distance):
    stack = []
    for i in range(N):
        if not stack or Location[i] - stack[-1] >= min_distance:
            stack.append(Location[i])

    return len(stack)

while Start <= End:
    mid = (Start + End) // 2
    if placeModem(mid) >= C:
        Start = mid + 1
    else:
        End = mid - 1

print( End )