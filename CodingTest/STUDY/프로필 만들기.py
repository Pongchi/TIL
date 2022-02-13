import string

def solution(name_list):
    name_dict = { name : 0 for name in set(name_list) }
    result = []
    
    for name in name_list:
        result.append( name + string.ascii_uppercase[name_dict[name]] )
        name_dict[name] += 1

    return result

print( solution(["김비바", "김비바", "이비바", "김토스", "이비바", "김비바"]) )
