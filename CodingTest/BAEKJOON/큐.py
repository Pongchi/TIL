import sys

N = int(sys.stdin.readline())
queue = []

def _push(n):
    queue.append(n)

def _size():
    return len(queue)

def _empty():
    return 0 if _size() else 1

def _pop():
    return queue.pop(0) if _size() else -1 

def _front():
    return queue[0] if _size() else -1

def _back():
    return queue[-1] if _size() else -1

def interpret(cmd):
    return eval("_" + cmd[0] +"()")

for i in range(N):
    cmd = sys.stdin.readline().split()
    if cmd[0] == "push":
        _push(cmd[1])
    else:
        print( interpret(cmd) )
        
