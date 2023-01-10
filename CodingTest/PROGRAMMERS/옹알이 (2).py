def solution(babbling):
    result = 0
    for bab in babbling:
        i = 0
        q = 0
        while i < len(bab):
            if bab[i] == 'a' and len(bab) -i > 2 and bab[i+1:i+3] == 'ya' and q != 1:
                i += 3
                q = 1
                
            elif bab[i] == 'y' and len(bab) -i > 1 and bab[i+1] == 'e' and q != 2:
                i += 2
                q = 2
                
            elif bab[i] == 'w' and len(bab) -i > 2 and bab[i+1:i+3] == 'oo' and q != 3:
                i += 3
                q = 3
            
            elif bab[i] == 'm' and len(bab) -i > 1 and bab[i+1] == 'a' and q != 4:
                i += 2
                q = 4
                
            else:
                break
        else:
            result += 1
                
    return result
