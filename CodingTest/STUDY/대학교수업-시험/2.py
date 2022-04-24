import sys

if __name__ == '__main__':
    a, b = map(int, sys.stdin.readline().split())
    msg = sys.stdin.readline()[:-1]

    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
                'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                'u', 'v', 'w', 'x', 'y', 'z']
    
    decode = {}
    for i in range(26):
        ch = alphabet[i]
        encode = alphabet[(a * i + b) % 26]
        decode[encode] = ch
    
    ans = ''
    for m in msg:
        ans += decode[m]
    print(ans)