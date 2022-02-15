# 문제 주소 : https://www.acmicpc.net/problem/1300

N = int(input())
k = int(input())

Start = 1
End = N * N
while Start <= End:
    mid = (Start + End) // 2
    tmp = 0
    for row in range(1, N+1):
        tmp += min(mid//row, N)

    if tmp >= k:
        result = mid
        End = mid - 1
    else:
        Start = mid + 1

print( result )