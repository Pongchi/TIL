E, S, M = list(map(int, input().split()))

years = 1
_E, _S, _M = (1, 1, 1)
while (E, S, M) != (_E, _S, _M):
    _E, _S, _M = (_E+1, _S+1, _M+1)
    if _E > 15:
        _E = 1
    if _S > 28:
        _S = 1
    if _M > 19:
        _M = 1
    years += 1

print( years )