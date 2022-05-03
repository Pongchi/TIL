# 문제 주소 : https://programmers.co.kr/learn/courses/30/lessons/87390
# 처음에 for 문 n번 돌려서 했지만 시간초과가 뜨기에 방법을 찾는 중 패턴을 찾을 수 있었음.

def solution(n, left, right):
    return [ max(i//n, i%n)+1 for i in range(left, right+1) ]