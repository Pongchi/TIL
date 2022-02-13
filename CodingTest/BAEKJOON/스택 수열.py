import sys

N = [ i+1 for i in range(int(sys.stdin.readline()))]
lst = [ int(sys.stdin.readline()) for i in range(len(N)) ]
N_idx = 0
lst_idx = 0
stack = []
result_stack = []

while True:
    print(stack)
    if lst_idx == len(lst):
        break
    elif len(stack) == 0:
        stack.append(N[N_idx])
        N_idx += 1
        result_stack.append("+")
    
    elif stack[-1] == lst[lst_idx]:
        stack.pop()
        lst_idx += 1
        result_stack.append("-")
        
    elif N_idx == len(N):
        break
    
    else:
        stack.append(N[N_idx])
        N_idx += 1
        result_stack.append("+")

if len(stack) == 0:
    for _ in result_stack:
        print(_)
else:
    print("NO")
