# 문제 주소 : https://www.acmicpc.net/problem/2805
# 문제 분류 : 이분 탐색, 매개 변수 탐색
# 풀이 방법 : 길이에 따른 얻을 수 있는 함수를 정의한 뒤에 이분탐색의 기본적인 알고리즘으로 계속 탐색.
# 풀이 소요 시간 : 약 15분( 전에 이분 탐색 문제를 풀어본적이 있어서 그 코드를 바탕으로 재구성함. )

N, M = map(int, input().split())
Trees = list(map(int, input().split()))
Start = 1
End = max(Trees)

def EarnWood(length):
    return sum([ Tree - length if Tree - length >= 0 else 0 for Tree in Trees])

while Start <= End:
    mid = (Start + End) // 2
    if EarnWood(mid) >= M:
        Start = mid + 1
    else:
        End = mid - 1

print(End)