#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if (idx < 0 or idx > (len(my_list) - 1)):
        return(None)
    else:
        new_list = my_list[0:idx] + my_list[(idx + 1):]
        new_list.insert(idx, element)
        return(new_list)
