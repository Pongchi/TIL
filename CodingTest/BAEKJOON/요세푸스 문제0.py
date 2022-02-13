N, K = map(int, input().split())

Sequence = [str(i+1) for i in range(N)]
result = []
cIdx = 0

for i in range(N):
    cIdx = (cIdx + K-1) % len(Sequence)
    result.append( Sequence.pop(cIdx) )
print( "<" + ", ".join(result) + ">")