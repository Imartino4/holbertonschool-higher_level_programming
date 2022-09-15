#!/usr/bin/python3
def weight_average(my_list=[]):
    r1 = 0
    r2 = 0
    if my_list:
        for i in my_list:
            r1 = r1 + i[1]
            r2 = r2 + i[0]*i[1]
        return r2/r1
    return 0
