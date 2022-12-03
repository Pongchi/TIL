# 문제 주소 : https://www.acmicpc.net/problem/1043

import sys

def input():
    return sys.stdin.readline().rstrip()

N, M = map(int, input().split())
known_persons = set(map(int, input().split()[1:]))
partys = [ set(map(int, input().split()[1:])) for party in range(M) ]

result = 0
for participating_persons in sorted(partys, key=lambda x : -len(x)):
    if len(known_persons & participating_persons) == 0:
        result += 1
    
    else:
        known_persons = known_persons.union(participating_persons)
    
print( result )