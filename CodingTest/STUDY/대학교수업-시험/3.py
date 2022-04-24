import sys

if __name__ == '__main__':
    N = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))
    ans = 0

    for i in range(N-2):
        for j in range(i+1, N-1):
            for k in range(j+1, N-2):
                kcal = arr[i] + arr[j] + arr[k]
                if kcal >= 2000 and kcal <= 2500:
                    ans += 1
    print(ans)