N = int(input())
distance = list(map(int, input().split()))
price = list(map(int, input().split()))
result = 0

i = 0
while i < N-1:
    j = i + 1
    while price[i] < price[j]:
        if j > N-2:
            break
        j += 1

    result += sum([ distance[x] for x in range(i, j)]) * price[i]
    i = j
    
print( result )