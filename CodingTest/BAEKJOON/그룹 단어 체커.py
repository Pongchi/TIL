N = int(input())
WORDS = [input() for i in range(N)]
cnt = 0

for WORD in WORDS:
    isUsed = {'a': False, 'b': False, 'c': False, 'd': False, 'e': False, 'f': False, 'g': False, 'h': False, 'i': False, 'j': False, 'k': False, 'l': False, 'm': False, 'n': False, 'o': False, 'p': False, 'q': False, 'r': False, 's': False, 't': False, 'u': False, 'v': False, 'w': False, 'x': False, 'y': False, 'z': False}
    prevA = WORD[0]
    
    for i in WORD+"!":
        if i == "!":
            cnt += 1
        elif (not isUsed[i]) or prevA == i:
            isUsed[i] = True
        else:
            break
        prevA = i
    
print(cnt)
