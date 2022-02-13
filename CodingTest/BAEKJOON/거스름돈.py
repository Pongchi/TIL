cost = 1000 - int(input())
result = 0

for coin in [500, 100, 50, 10, 5, 1]:
    if cost >= coin:
        result, cost = (result + cost // coin, cost%coin)
    
    if cost == 0:
        break

print( result )