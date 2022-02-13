T = int(input())
KN = tuple( tuple(map(int, (input(), input()))) for i in range(T) )

def MEMBER(k, n):
    apart = [ [] if i != 0 else [j for j in range(1, n+1) ] for i in range(k+1) ]
    for i in range(k):
	    for j in range(n):
		    apart[i+1].append( sum(apart[i][:j+1]) )
    print(apart[k][n-1])
    
for k, n in KN:
    MEMBER(k, n)
