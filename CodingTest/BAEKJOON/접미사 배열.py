S = input()
suffix = sorted([ S[i:] for i in range(len(S)) ])

print( "\n".join(suffix) )
