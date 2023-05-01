import math

def solution(fees, records):
    answer1 = {}
    parking = {}
    
    for i in range(len(records)) :
        record = records[i].split()
        
        if record[2] == "IN" :
            time = int(record[0][: 2]) * 60 + int(record[0][3 : 5])
            parking[record[1]] = time
        else :
            out_time = int(record[0][: 2]) * 60 + int(record[0][3 : 5])
            if record[1] in answer1 :
                answer1[record[1]] += out_time - parking[record[1]]
            else :
                answer1[record[1]] = out_time - parking[record[1]]
            parking.pop(record[1], None)
        
        if (i == len(records) - 1) and (parking) :
            for j, k in parking.items() :
                out_time = 1439 - k
                if j in answer1 :
                    answer1[j] += out_time
                else :
                    answer1[j] = out_time
    
    answer2 = []
    for m, n in sorted(answer1.items()) :
        if n <= fees[0] :
            answer2.append(fees[1])
        else :
            answer2.append(fees[1] + math.ceil((n - fees[0]) / fees[2]) * fees[3])
        
    return answer2


# 다른 사람의 풀이
from collections import defaultdict
from math import ceil

class Parking:
    def __init__(self, fees):
        self.fees = fees
        self.in_flag = False
        self.in_time = 0
        self.total = 0

    def update(self, t, inout):
        self.in_flag = True if inout=='IN' else False
        if self.in_flag:  self.in_time = str2int(t)
        else:             self.total  += (str2int(t)-self.in_time)

    def calc_fee(self):
        if self.in_flag: self.update('23:59', 'out')
        add_t = self.total - self.fees[0]
        return self.fees[1] + ceil(add_t/self.fees[2]) * self.fees[3] if add_t >= 0 else self.fees[1]

def str2int(string):
    return int(string[:2])*60 + int(string[3:])

def solution(fees, records):
    recordsDict = defaultdict(lambda:Parking(fees))
    for rcd in records:
        t, car, inout = rcd.split()
        recordsDict[car].update(t, inout)
    return [v.calc_fee() for k, v in sorted(recordsDict.items())]