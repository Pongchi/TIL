def Hanoi(n, from_pos, to_pos, aux_pos):
    if n == 1:
        return print(from_pos, to_pos)
    
    Hanoi(n-1, from_pos, aux_pos, to_pos)
    print(from_pos, to_pos)
    Hanoi(n-1, aux_pos, to_pos, from_pos)
    
N = int(input())

print(2 ** N - 1)
Hanoi(N, 1, 3, 2)
