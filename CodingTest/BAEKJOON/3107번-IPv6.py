# 문제 주소 : https://www.acmicpc.net/problem/3107

split_IPv6 = list(map(lambda x : x.split(':'), input().split('::')))
IPv6 = split_IPv6[0][:]

if len(split_IPv6) == 2:
    for i in range(8-len(IPv6)-len(split_IPv6[1])):
        IPv6.append('0000')
    for i in split_IPv6[1]:
        IPv6.append(i)

print(":".join(map(lambda x : x.zfill(4), IPv6)))