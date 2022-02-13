MAX = 10000
LIST = [ i for i in range(1, MAX+1) ]

for i in [ i for i in range(1, MAX+1) ]:
    gen_Num = (lambda n: n + sum(map(int, str(n))))(i)
    if len(LIST) < gen_Num:
        continue
    LIST[gen_Num-1] = False

for i in [ i for i in LIST if i != False or i > MAX]:
    print(i)
