import sys

L = int(sys.stdin.readline())
r = 31
M = 1234567891

H = sum([(ord(s) - 96) * (r ** idx) for idx, s in enumerate(sys.stdin.readline().rstrip()) ]) % M
print( H )
