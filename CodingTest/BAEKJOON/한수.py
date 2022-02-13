def isHan(n):
    if n < 100:
        return True
    elif n == 1000:
        return False
    else:
        return True if 2*int(str(n)[1]) == int(str(n)[0])+int(str(n)[2]) else False

N = int(input())
cnt = 0

for i in range(1, N+1):
    if isHan(i):
        cnt += 1

print(cnt)
