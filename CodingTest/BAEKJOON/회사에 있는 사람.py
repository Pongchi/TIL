import sys

n = int(sys.stdin.readline())
Company = dict()

for i in range(n):
    name, cmd = sys.stdin.readline().split()
    if cmd == "enter":
        Company[name] = True
    else:
        del Company[name]
        
print( "\n".join( sorted([ name for name in Company ], reverse=True) ))
