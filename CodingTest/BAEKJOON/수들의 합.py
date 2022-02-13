S = int(input())

for i in range(1, S+1):
    S -= i
    if S <= 0:
        print(i-1 if S != 0 else i)
        break