N = sorted(map(int, input()), reverse=True)

if N[-1] != 0:
    print(-1)
else:
    result = "".join(map(str, N))
    print( result if int(result) % 30 == 0 else -1 )
