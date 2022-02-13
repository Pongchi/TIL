import sys

N = int(sys.stdin.readline())
Lst = [ tuple(map(int, sys.stdin.readline().split())) for i in range(N) ]
Lst = sorted(Lst, key=lambda x : (x[1], x[0]))
result = 0
End_Time = 0
print(Lst)

for x, y in Lst:
    if End_Time > x or End_Time > y:
        continue
    result += 1
    End_Time = y

print( result )
