from collections import Counter

N = int(input())
Lst = sorted(tuple( int(input()) for i in range(N) ))
_Lst = Counter(Lst).most_common()

print( int(round(sum(Lst) / len(Lst), 0)) )
print( Lst[((len(Lst)+1) // 2) - 1 ])
print( (_Lst[0][0] if _Lst[0][1] != _Lst[1][1] else _Lst[1][0]) if len(_Lst) != 1 else _Lst[0][0] )
print( Lst[-1] - Lst[0] )
