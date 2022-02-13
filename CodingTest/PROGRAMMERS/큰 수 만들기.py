def solution(number, k):
    number = list(number)
    idx = 0
    for _ in range(k):
        L = len(number)
        for i in range(idx, len(number)-1):
            if number[i] < number[i+1]:
                number.pop(i)
                idx = i-1 if i-1 >= 0 else 0
                break
                
        if L == len(number):
            number.pop()
        
    return "".join(number)

print( solution("1924", 2) )