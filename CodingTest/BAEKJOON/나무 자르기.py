N, M = map(int, input().split())
Trees = list(map(int, input().split()))
i = sum(Trees) // N
result = -1

def EarnWood(length):
    return sum([ Tree - length if Tree - length >= 0 else 0 for Tree in Trees])

while M != result:
    pass