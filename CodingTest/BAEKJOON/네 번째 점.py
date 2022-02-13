XY = tuple( tuple(map(int, input().split())) for i in range(3) )
X = ({XY[0][0], XY[1][0]} - {XY[2][0]}).pop() if len({XY[0][0], XY[1][0]}) == 2 else XY[2][0]
Y = ({XY[0][1], XY[1][1]} - {XY[2][1]}).pop() if len({XY[0][1], XY[1][1]}) == 2 else XY[2][1]

print(X, Y)
