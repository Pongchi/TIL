# 아래의 코드는 시간복잡도를 신경쓰지 않고 짠 코드. But, 시간초과가 뜨길래 약수 구하는 부분을 고쳐 다시 코드를 짜기로함.
# def calc_divisor(n):
#     return len([ i for i in range(1, n+1) if n % i == 0 ])

# def solution(number, limit, power):
#     def setDamage(n):
#         return n if n <= limit else power
    
#     return sum([ setDamage(calc_divisor(i))  for i in range(1, number+1) ])
