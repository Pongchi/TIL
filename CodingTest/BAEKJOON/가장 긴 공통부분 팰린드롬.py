import sys

n = int(sys.stdin.readline())
S_lst = []
min_s = "1" * 1000001
felin = []
min_i = 0

def isFelin(s: str) -> bool:
    l = len(s)
    for i in range(l//2+1):
        if s[i] != s[l-i-1]:
            return False
    return True

def all_is_in(F):
    for S in S_lst:
        if F not in S:
            return False
    return True

for i in range(n):
    s = sys.stdin.readline().rstrip()
    S_lst.append(s)
    if len(min_s) > len(s):
        min_s = s
        min_i = i
        
print(min_s)

del S_lst[min_i]
for i in range(len(min_s)-1, -1, -1):
    for j in range(len(min_s)-i):
        data = min_s[j:j+i+1]
        if isFelin(data):
            felin.append(data)

print(felin)

for F in felin:
    if all_is_in(F):
        print(len(F))
        exit(0)

print(0)
