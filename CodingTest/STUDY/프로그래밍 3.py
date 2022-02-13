import math

def solution(fees, records):
    def subTime(time1, time2):
        time1 = list(map(int, time1.split(':')))
        time2 = list(map(int, time2.split(':')))
        result = 0

        if time2[1] >= time1[1]:
            result += time2[1] - time1[1]
        else:
            time2[0] -= 1
            result += 60 + time2[1] - time1[1]

        result += (time2[0] - time1[0]) * 60
        return result

    def cal_fees(accum_time):
        return fees[1] if diff_time <= fees[0] else int(fees[1] + ((diff_time - fees[0]) / fees[2]) * fees[3])

    IO_num = {}
    accum_time = {}

    for record in records:
        rec = record.split()

        if rec[2] == "IN":
            IO_num[rec[1]] = rec[0]
            if rec[1] not in accum_time:
                accum_time[rec[1]] = 0

        else:
            accum_time[rec[1]] += subTime()


    return []


print( solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]) )