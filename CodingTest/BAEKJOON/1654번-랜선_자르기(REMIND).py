# 문제 주소 : https://www.acmicpc.net/problem/1654

import sys

N, K = map(int, sys.stdin.readline().split())
LANs = list(map(int, [ sys.stdin.readline() for _ in range(N) ]))
START = 0
END = max(LANs)

def Count(length):
    if length == 0:
        return sum(LANs)

    count = 0
    for LAN in LANs:
        count += LAN // length
    return count

while START <= END:
    MID = (START + END) // 2
    if Count(MID) < K:
        END = MID - 1
    else:
        START = MID + 1

print(END)