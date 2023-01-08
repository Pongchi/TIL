# Lv.0 옹알이 (1)
# 파이썬의 기능을 이용해 시간복잡도는 고려하지 않고 함.

def solution(babbling):
    pronounceables = ["aya", "ye", "woo", "ma"]
    result = 0
    
    for word in babbling:
        if 1 < len(word) < 11:
            check = len(word)
            for pronounceable in pronounceables:
                if pronounceable in word:
                    check -= len(pronounceable)
            result += 1 if check == 0 else 0
            
    return result
