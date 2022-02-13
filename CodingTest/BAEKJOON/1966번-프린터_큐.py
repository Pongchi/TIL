# 문제 주소 : https://www.acmicpc.net/problem/1966
# 문제 분류 : 구현, 자료 구조, 시뮬레이션, 큐
# 풀이 방법 : (인덱스, 중요도) 로 이루어진 리스트A와 중요도를 기준을 정렬한 또 다른 리스트B를 1개 만든다.
#           그리고 A리스트의 0번째의 중요도가 B의 -1번째 중요도와 같다면 B의 -1번째는 pop한다.
#           또한 A리스트의 0번째도 pop을 하는데 그 결과값의 인덱스가 M과 같다면 반복을 멈추고 몇번째로 
#           출력되는지 반환.
# 풀이 소요 시간 : 약 1시간.. 생각을 빨리 정리하지 못해서 계속 삽질좀 했음.

import sys

for t in range(int(sys.stdin.readline())):
    N, M = map(int, sys.stdin.readline().split())
    Priority = [(i, P) for i, P in enumerate(sys.stdin.readline().split())]
    sort_P = sorted(Priority, key=lambda x : x[1])
    i = 0
    while True:
        if Priority[0][1] == sort_P[-1][1]:
            i += 1
            sort_P.pop()
            if Priority.pop(0)[0] == M:
                break
        else:
            Priority.append(Priority.pop(0))

    print( i )