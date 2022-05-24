# 문제 주소 : https://www.acmicpc.net/problem/5021

N, M = map(int, input().split())
KING = input()
blood = {KING : 1.0}
for _ in range(N):
    child, parent1, parent2 = input().split()
    blood[child] = (blood.get(parent1, 0.0) + blood.get(parent2, 0.0)) / 2

result = input()
for _ in range(M-1):
    name = input()
    if blood.get(name, 0.0) < blood.get(name, 0.0):
        result = name

print( name )