import sys

total = 0
Trees = dict()

while True:
    tree = sys.stdin.readline().rstrip()
    if not tree:
        break
    
    total += 1
    if tree not in Trees:
        Trees[tree] = 0
    Trees[tree] += 1
            
for tree in sorted(Trees):
    print(tree, "%.4f" % round(Trees[tree] / total * 100, 4))
