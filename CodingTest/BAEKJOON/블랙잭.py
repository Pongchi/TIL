from itertools import combinations

N, M = map(int, input().split())
Cards = tuple(map(int, input().split()))
print( max( tuple( sum((x, y, z)) for x,y,z in combinations(Cards, 3) if sum((x,y,z)) <= M )))
