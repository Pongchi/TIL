# 문제 주소 : https://programmers.co.kr/learn/courses/30/lessons/42583

def solution(bridge_length, weight, truck_weights):
    result = 0
    bridge = [0] * bridge_length
    
    while bridge:
        result += 1
        bridge.pop(0)
        
        if truck_weights:
            if sum(bridge) + truck_weights[0] <= weight:
                bridge.append( truck_weights.pop(0) )
            else:
                bridge.append(0)
        
    return result