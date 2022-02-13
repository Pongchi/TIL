N = int(input())
XY = tuple(tuple(map(int, input().split())) for i in range(N))
result = []

for x, y in XY:
    cnt = 0
    for _x, _y in XY:
        if x == _x and y == _y:
            continue
        elif x < _x and y < _y:
            cnt += 1
            
    result.append(str(cnt+1))

print(" ".join(result))
