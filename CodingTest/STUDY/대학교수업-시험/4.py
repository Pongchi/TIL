import sys

if __name__ == '__main__':
    a, b = map(int, sys.stdin.readline().split())
    N = int(sys.stdin.readline())
    arr = [a, b]
    for n in range(N):
        arr += list(map(int, sys.stdin.readline().split()))
        arr.sort()
        print(arr[n+1], arr[2*n+3])