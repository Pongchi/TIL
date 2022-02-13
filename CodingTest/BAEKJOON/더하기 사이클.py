A = int(input())
cnt = 0
B = -1

def add(num):
    if num < 10:
        num *= 10
    if num == 0:
        return 0
    
    strNum = str(num) 
    return int( strNum[-1] + str(sum(map(int, strNum)))[-1] )

while A != B:
    cnt += 1
    if cnt == 1:
        B = add(A)
    else:
        B = add(B)

    print(B)
print(cnt)
