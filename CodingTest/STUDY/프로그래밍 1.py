def solution(id_list, report, k):
    reported = { name: 0 for name in id_list }
    result = dict(reported)
    report = set(report) # 중복 신고 없애기
    banned = []

    for i in report:  # 신고 당한횟수 늘리고 정지 당한 사람 추가
        i = i.split()
        reported[i[1]] += 1
        if reported[i[1]] >= k:
            banned.append(i[1])

    for i in report: # 정지당한 사람을 신고했는지
        i = i.split()
        if i[1] in banned:
            result[i[0]] += 1

    return list(result.values())

print( solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2))
print( solution(["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3))