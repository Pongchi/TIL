T = int(input())
result = []

for time in [300, 60, 10]:
    result.append(T//time)
    T = T%time

print( " ".join(map(str, result)) if T == 0 else -1 )