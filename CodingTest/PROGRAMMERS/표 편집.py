# 문제 주소 : https://programmers.co.kr/learn/courses/30/lessons/81303

def solution(n, k, command):
    stack = []
    arr = list(range(n))
    def undo(number):
        if arr[-1] < number:
            arr.append(number)
        else:
            for i in range(len(arr)-1, -1, -1):
                if arr[i] < number:
                    arr.insert(i+1, number)
                    return
    
    for cmd in command:
        cmd = cmd.split()
        if cmd[0] == 'U':
            k -= int(cmd[1])

        elif cmd[0] == 'D':
            k += int(cmd[1])
        
        elif cmd[0] == 'C':
            stack.append(arr.pop(k))
            k += 0 if k < len(arr)-1 else -1
            
        else:
            undo(stack.pop())
    
    result = ''
    i = 0
    while i < len(arr):
        if arr[i] == len(result):
            result += 'O'
            i += 1
        else:
            result += 'X'

    return result

print( solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]) ) # "OOOOXOOO"
print( solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]) ) # "OOXOXOOO"