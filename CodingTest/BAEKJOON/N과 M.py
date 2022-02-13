from itertools import permutations

N, M = map(int, input().split())
Lst = tuple( str(i) for i in range(1, N+1) )
for i in tuple(permutations(Lst, M)):
    print( " ".join(i) )
