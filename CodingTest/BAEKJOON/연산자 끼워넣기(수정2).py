import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
OpersCnt = list(map(int, sys.stdin.readline().split()))
_max = -1000000001
_min = 1000000001

def dfs(depth, result, plus, minus, multiply, divide):
    global _max, _min
    if depth == N:
        _max = max(result, _max)
        _min = min(result, _min)
        return
    
    if plus:
        dfs(depth+1, result + arr[depth], plus-1, minus, multiply, divide)
    if minus:
        dfs(depth+1, result - arr[depth], plus, minus-1, multiply, divide)
    if multiply:
        dfs(depth+1, result * arr[depth], plus, minus, multiply-1, divide)
    if divide:
        dfs(depth+1, int(result / arr[depth]), plus, minus, multiply, divide-1)

dfs(1, arr[0], OpersCnt[0], OpersCnt[1], OpersCnt[2], OpersCnt[3])
print( f"{_max}\n{_min}")