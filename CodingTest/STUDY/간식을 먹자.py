def solution(limit_seconds):
    Foods = {300:10, 130:30, 120:20, 20:30}
    result = 0
    
    for food in Foods:
        while limit_seconds >= food:
            if Foods[food] > 0:
                result += 1
                limit_seconds -= food
                Foods[food] -= 1
            else:
                break

    return result

print( solution(450) )
