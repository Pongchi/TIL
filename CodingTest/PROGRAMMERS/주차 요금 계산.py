# 문제 주소 : https://programmers.co.kr/learn/courses/30/lessons/92341

from math import ceil

def diff_time(a, b):
        a_h, a_m = map(int, a.split(':'))
        b_h, b_m = map(int, b.split(':'))
        return ((b_h-a_h)*60 + b_m-a_m) if b_m >= a_m else ((b_h-a_h-1)*60 + b_m-a_m+60)
    
def solution(fees, records):
    def calcFee(m):
        return fees[1] + (0 if m <= fees[0] else (ceil((m-fees[0])/fees[2]))*fees[3])
                          
    rec = {}
    result = {}
    
    for record in records:
        time, car_number, io = record.split()
        
        if io == "IN":
            rec[car_number] = time
            if car_number not in result:
                result[car_number] = 0
        else:
            result[car_number] += diff_time(rec[car_number], time)
            del rec[car_number]
            
    for car_number in rec:
        result[car_number] += diff_time(rec[car_number], "23:59")
        
    for car_number in result:
        result[car_number] = calcFee(result[car_number])
    return [ i[1] for i in sorted(result.items()) ]