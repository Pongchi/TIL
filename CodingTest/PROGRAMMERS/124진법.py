def solution(n):
    answer = ''
    if n > 3: 
        while n > 3:
            answer = str(n%3) + answer
    else:
        answer= str(n)
    return answer.replace('3', '4')


print("1", solution(1))
print("2", solution(2))
print("3", solution(3))
print("4", solution(4))
