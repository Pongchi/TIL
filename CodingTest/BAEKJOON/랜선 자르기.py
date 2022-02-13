import sys

K, N = map(int, sys.stdin.readline().split())
LAN = [ int(sys.stdin.readline()) for i in range(K) ]
Start, End = 1, max(LAN)

def CountLAN(length):
    return sum([ L // length for L in LAN])

while Start <= End:
    mid = (Start + End) // 2
    if CountLAN(mid) >= N:
        Start = mid + 1
    else:
        End = mid - 1

print(End)