def hanoi(n, pos1, tmp, pos2):
    if n == 1:
        print(f"{pos1} -> {pos2}")
    else:
        hanoi(n-1, pos1, pos2, tmp)
        print(f"{pos1} -> {pos2}")
        hanoi(n-1, tmp, pos1, pos2)

hanoi(3, 'A', 'B', 'C')