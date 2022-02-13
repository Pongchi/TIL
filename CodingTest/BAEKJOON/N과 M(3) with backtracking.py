import sys

N, M = map(int, sys.stdin.readline().split())
N_lst = [ str(i) for i in range(1, N+1) ]
Lst = ['0']

def back_search():
    if len(Lst) == M+1:
        return print(' '.join(Lst[1:]))
    else:
        for i in N_lst:
            if Lst[-1] <= i:
                Lst.append(i)
                back_search()
                Lst.pop()

back_search()
