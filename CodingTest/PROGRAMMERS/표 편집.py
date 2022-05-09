# 문제 주소 : https://programmers.co.kr/learn/courses/30/lessons/81303

def solution(n, k, command):
    stack = []
    arr = list(range(n))
    def undo(number):
        if not arr or arr[-1] < number:
            arr.append(number)
        else:
            for i in range(len(arr)):
                if arr[i] > number:
                    arr.insert(i, number)
                    return
    
    for cmd in command:
        cmd = cmd.split()
        if cmd[0] == 'U':
            k -= int(cmd[1])

        elif cmd[0] == 'D':
            k += int(cmd[1])
        
        elif cmd[0] == 'C':
            stack.append(arr.pop(k))
            if arr and (stack[-1] > arr[-1]):
                k -= 1
            
        else:
            history = stack.pop()
            if arr[k] > history:
                k += 1
            undo(history)
    
    result = ""
    for i in arr:
        while len(result) != i:
            result += "X"
        result += "O"
    return result + "X"*(n-len(result))
        

print( solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]) ) # "OOOOXOOO"
print( solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]) ) # "OOXOXOOO"
print( solution(8, 0, ["C", "C", "C", "C", "C", "C", "C", "C"]))