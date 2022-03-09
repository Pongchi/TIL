# 문제 주소 : https://www.acmicpc.net/problem/2480

dice = dict()
for i in input().split():
    i = int(i)
    if i not in dice:
        dice[i] = 0
    dice[i] += 1

for k in dice:
    if dice[k] == 3:
        print(10000 + k * 1000 )
        exit()

    elif dice[k] == 2:
        print(1000 + k * 100)
        exit()

print( max(dice.keys()) * 100 )