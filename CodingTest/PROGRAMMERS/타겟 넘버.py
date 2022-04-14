def solution(numbers, target):
    answer = []
    def dfs(total, idx):
        if idx == len(numbers):
            if total == target:
                answer.append(0)
            return
        
        dfs(total+numbers[idx], idx+1)
        dfs(total-numbers[idx], idx+1)
        return
    
    dfs(0, 0)
    return len(answer)