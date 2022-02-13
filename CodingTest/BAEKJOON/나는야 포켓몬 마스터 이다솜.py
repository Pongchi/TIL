import sys

N, M = map(int, sys.stdin.readline().split())

pokemons_n = { i+1:sys.stdin.readline().rstrip() for i in range(N) }
pokemons_s = { value:key for key, value in pokemons_n.items() }

for i in range(M):
    search = sys.stdin.readline().rstrip()
    if search.isdigit():
        print( pokemons_n[int(search)] )
    else:
        print( pokemons_s[search] )
