import sys

N, M = map(int, sys.stdin.readline().split())
N_lst = [ str(i) for i in range(1, N+1) ]

def back_search(Lst):
    if len(Lst) != M:
        for i in N_lst:
            if not i in Lst:
                back_search(Lst + [i])
            else:
                return

    else:
        return print(" ".join(Lst))

back_search([])
