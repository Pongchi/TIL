N = int(input())
result = [0]

def hanoi(n, pos1, tmp, pos2):
    if n == 1:
        result[0] += 1
        if N <= 20:
            result.append(f'{pos1} {pos2}')
    else:
        hanoi(n-1, pos1, pos2, tmp)
        result[0] += 1
        if N <= 20:
            result.append(f'{pos1} {pos2}')
        hanoi(n-1, tmp, pos1, pos2)

hanoi(N, 1, 2, 3)
print( "\n".join(map(str, result)) )