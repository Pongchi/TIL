# 문제 주소 : https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AX8BAN1qTwoDFARO&categoryId=AX8BAN1qTwoDFARO&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=3&pageSize=10&pageIndex=1&&&&&&&&&&

def isExistSquare(N, square):
    for i in range(N-1):
        for j in range(N-1):
            if square[i][j] == '#' and square[i+1][j] == '#' and square[i][j+1] == '#' and square[i+1][j+1] == '#':
                return True
    return False

for T in range(int(input())):
    N = int(input())
    print(f"#{T+1} yes" if isExitSquare(N, [input() for i in range(N)]) else f"#{T+1} no")