# 문제 주소 : https://programmers.co.kr/learn/courses/30/lessons/81303

def solution(n, k, command):
    stack = []
    arr = [ 1 for i in range(n) ]
    def TOP():
        for i in range(n-1, -1, -1):
            if arr[i]:
                return i
        return 0
    
    for cmd in command:
        cmd = cmd.split()
        if cmd[0] == 'U':
            cnt = int(cmd[1])
            while cnt:
                if arr[k-1]:
                    cnt -= 1
                k -= 1

        elif cmd[0] == 'D':
            cnt = int(cmd[1])
            while cnt:
                if arr[k+1]:
                    cnt -= 1
                k += 1
        
        elif cmd[0] == 'C':
            arr[k] = 0
            stack.append(k)
            k += 1 if k < TOP() else -1
            
        else:
            arr[stack.pop()] = 1
    
    result = ""
    for value in arr:
        result += 'O' if value else 'X'
    return result

print( solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]) ) # "OOOOXOOO"
