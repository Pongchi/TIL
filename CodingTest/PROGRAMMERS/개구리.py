def solution(stones):
    cnt = 0
    current = 0
    n = len(stones)
    while current < n:
        current += stones[current]
        print(current)
        cnt += 1
    return cnt

solution([2, 5, 1, 3, 2, 1])
