import sys

N = int(sys.stdin.readline())
arr = sys.stdin.readline().split()
OpersCnt = list(map(int, sys.stdin.readline().split()))
max_operator = ["-"] * OpersCnt[1] + ["/"] * OpersCnt[3] + ["+"] * OpersCnt[0] + ["*"] * OpersCnt[2]
if OpersCnt[1]:
    min_operator = ["*"] * OpersCnt[2] + ["+"] * OpersCnt[0] + ["-"] * OpersCnt[1] + ["/"] * OpersCnt[3] 
else:
    min_operator = ["*"] * OpersCnt[2] + ["+"] * OpersCnt[0] + ["-"] * OpersCnt[1] + ["/"] * OpersCnt[3] 

_max = arr[0]
_min = arr[0]
for i in range(N-1):
    _max = int(eval(str(_max) + max_operator[i] + arr[i+1]))
    _min = int(eval(str(_min) + min_operator[i] + arr[i+1]))

print(f"{_max}\n{_min}")