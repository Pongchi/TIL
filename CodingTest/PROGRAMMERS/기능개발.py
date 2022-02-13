def solution(progresses, speeds):
    release_date = [ (100 - progresses[i]) // speeds[i] if ((100 - progresses[i]) / speeds[i]) % 1 == 0 else int((100 - progresses[i]) / speeds[i])+1 for i in range(len(progresses)) ]
    today = 1
    func = 0
    answer = []
    
    while len(release_date) > func:
    
        if release_date[func] > today:
            today += 1; continue
            
        current_func = func
        for i in range(func, len(release_date)):
            if release_date[i] <= today:
                func += 1; continue
            else:
                answer.append(i - current_func)
                break

    return answer

print(solution([93, 30, 55], [1, 30, 5]))
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))
