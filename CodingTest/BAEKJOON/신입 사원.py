import sys

T = int(sys.stdin.readline())
for t in range(T):
    N = int(sys.stdin.readline())
    volunteer = [ tuple(map(int, sys.stdin.readline().split())) for i in range(N) ]
    _max = N+1
    result = 0
    for v in sorted(volunteer):
        if v[1] < _max:
            result += 1
            _max = v[1]
        print(v)
    print("=====================")
    print(result)
