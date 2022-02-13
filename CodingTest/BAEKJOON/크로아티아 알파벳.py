"""
CA = {"dz=":"1", "c=":"2", "c-":"3", "d-":"4", "lj":"5", "nj":"6", "s=":"7", "z=":"8"}
S = input()

for ca in CA:
    repl_S = S.replace(ca, CA[ca])
    if S != repl_S:
        S = repl_S

print(len(set(S)))
"""
CA = {"dz=":"1", "c=":"2", "c-":"3", "d-":"4", "lj":"5", "nj":"6", "s=":"7", "z=":"8"}
S = input()

for K,V in CA.items():
    S = S.replace(K, V)

print(len(set(S)))
