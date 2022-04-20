# 문제 주소 : https://programmers.co.kr/learn/courses/30/lessons/42839

from itertools import permutations

def isPrime(n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True if n > 1 else False

def solution(numbers):
    nums = []
    for i in range(1, len(numbers)+1):
        nums += [ int("".join(i)) for i in permutations(numbers, r=i) ]
    return len([ True for n in set(nums) if isPrime(n) ])