import sys

while True:
    try:
        A, B = map(int, sys.stdin.readline())
        print(A + B)
    except Error as ie:
        print(ie)
        break
