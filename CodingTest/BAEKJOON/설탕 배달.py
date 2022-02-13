N = int(input())

def Sugar(N):
    cnt = 0
    while N > 0:
        cnt += 1
        for i in range(1, N):
            if N - (3 * i) < 0 and N - (5 * i) < 0:
                return -1
            elif (N - (5 * i)) % 5 == 0 or (N - (5 * i)) % 3 == 0:
                N -= 5
                break
            elif (N - (3 * i)) % 5 == 0 or (N - (3 * i)) % 3 == 0:
                N -= 3
                break
    return cnt
            
print(Sugar(N))
