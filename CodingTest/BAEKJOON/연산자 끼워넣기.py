import sys
from itertools import permutations

N = int(sys.stdin.readline())
arr = sys.stdin.readline().split()
OpersCnt = list(map(int, sys.stdin.readline().split()))
operators = list(permutations(["+"] * OpersCnt[0] + ["-"] * OpersCnt[1] + ["*"] * OpersCnt[2] + ["/"] * OpersCnt[3], N-1))

_max = -1000000001
_min = 1000000001
for operator in operators:
    result = arr[0]
    for i in range(N-1):
        result = int(eval(str(result) + operator[i] + arr[i+1]))

    if _min > result:
        print(operator, result)
        _min = result
    if _max < result:
        _max = result

print( f"{_max}\n{_min}")