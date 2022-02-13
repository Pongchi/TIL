C = int(input())
datas = [tuple(map(int, input().split())) for i in range(C)]

for scores in datas:
    avg = sum(scores[1:]) / scores[0]
    cnt = 0

    for score in scores[1:]:
        if avg < score:
            cnt += 1

    ratio = cnt / scores[0] * 100
    print( str(round(ratio, 3)) + "%" if int(ratio) != ratio else str(int(ratio)) + ".000%" )
