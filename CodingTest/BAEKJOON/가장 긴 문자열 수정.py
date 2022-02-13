import sys

table = {}

def HASH(S):
    return sum([ ord(s) * (2 ** (len(S)-1 - idx)) for idx, s in enumerate(S)])

def solution(L, S):
    for i in range(L-1, 0, -1):
        for j in range(L-i+1):
            data = S[j:j+i]
            hashing = HASH(data)
            
            if table.get(hashing):
                return len(data)
                
            else:
                table[hashing] = data
                
    return 0

print( solution(int(sys.stdin.readline().rstrip()), sys.stdin.readline().rstrip()) )
