import sys

L = int(sys.stdin.readline().rstrip())
S = sys.stdin.readline().rstrip()
table = {}
max_length = 0

def HASH(S):
    return sum([ ord(s) * (2 ** (len(S)-1 - idx)) for idx, s in enumerate(S)])

for i in range(1, L):
    for j in range(L-i+1):
        data = S[j:j+i]
        hashing = HASH(data)
        
        if hashing in table:
            if max_length < len(data):
                max_length = len(data)
        else:
            table[hashing] = data

print( max_length )
