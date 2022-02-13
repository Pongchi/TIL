import sys

words = set([])
N = int(sys.stdin.readline())
for n in range(N):
    words.add(sys.stdin.readline().rstrip())

for word in sorted(words, key=lambda x:(len(x), x)):
    print(word)