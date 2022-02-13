import sys

N = int(sys.stdin.readline())
Lst = [ list(map(int, sys.stdin.readline().split())) for i in range(N) ]
result = [0, 0]

def make_paper(Lst):
    global result

    if len(Lst) > 1:
        for LST in Lst:
            for i in LST:
                if i != Lst[0][0]:
                    make_paper([ j[:len(Lst)//2] for j in Lst[:len(Lst)//2]])
                    make_paper([ j[len(Lst)//2:] for j in Lst[:len(Lst)//2]])
                    make_paper([ j[:len(Lst)//2] for j in Lst[len(Lst)//2:]])
                    return make_paper([ j[len(Lst)//2:] for j in Lst[len(Lst)//2:]])

    result[Lst[0][0]] += 1
    return
                

make_paper(Lst)
print("\n".join(map(str,result)))
