# 문제 주소 : https://www.acmicpc.net/problem/11723

import sys

class SET:
    def __init__(self):
        self.S = set()

    def add(self, x):
        self.S.add(x)

    def remove(self, x):
        self.S.discard(x)

    def toggle(self, x):
        if x in self.S:
            self.S.discard(x)
        else:
            self.S.add(x)
    
    def all(self):
        self.S = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}
    
    def empty(self):
        self.S.clear()

    def check(self, x):
        print(1 if x in self.S else 0)

############################################################################################3

S = SET()        
for _ in range(int(sys.stdin.readline())):
    cmd = sys.stdin.readline().split()
    if len(cmd) == 1:
        if cmd[0] == "all":
            S.all()
        else:
            S.empty()
    
    else:
        cmd[1] = int(cmd[1])
        if cmd[0] == "add":
            S.add(cmd[1])
        
        elif cmd[0] == "remove":
            S.remove(cmd[1])
        
        elif cmd[0] == "check":
            S.check(cmd[1])

        elif cmd[0] == "toggle":
            S.toggle(cmd[1])    