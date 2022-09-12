#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        max_ = my_list[0]
        for i in range(1, len(my_list)):
            if my_list[i] > max_:
                max_ = my_list[i]
        return max_
    else:
        return None
