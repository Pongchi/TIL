def solution(csv_string, keyword):
    organ_chart = [ string.split(',') for string in csv_string.split('\n') ]
    team_people = {team[0]: team[3] for team in organ_chart[1:]}

    for team in organ_chart:
        print(team)

    team_child = {team[0] : [] for team in organ_chart[1:]} # 각 팀의 하위 팀ID
    for team in organ_chart[2:]:
        team_child[team[2]].append(team[0])

    for team in organ_chart[1:]:  # 키워드가 들어간 팀 찾기.
        if keyword in team[1]:
            keyword_team = team
            break

    print("하위 팀", team_child)
    print("팀의 구성원 수", team_people)
    return 0

print( solution( """"조직 ID,조직명,상위 조직 ID,소속 팀원 수\n1,토스팀,,1\n2,인터널 트라이브,1,1\n3,인터널 매니저 팀,2,7\n4,비바 플랫폼 팀,2,14\n5,아웃터널 트라이브,1,2\n6,가이드 팀,5,4\n7,피트아웃 사일로,5,11""", "아웃" ) )