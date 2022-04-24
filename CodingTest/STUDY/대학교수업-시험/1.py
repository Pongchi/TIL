import sys

if __name__ == '__main__':
    N = int(sys.stdin.readline())
    arr = []
    for n in range(N):
        arr.append(sys.stdin.readline()[:-1])
    T = int(sys.stdin.readline())
    for _ in range(T):
        W = sys.stdin.readline()[:-1]
        ans = 0
        for n in range(N):
            if len(arr[n]) < len(W):
                continue
            flg = 1
            for lw in range(len(W)):
                if arr[n][lw] != W[lw]:
                    flg = 0
                    break
            ans += flg
        print(ans)