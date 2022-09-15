#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        count = 0
        for i in my_list:
            if count < x:
                print(f"{i}", end="")
                count = count + 1
        print(f"")
    except TypeError as message:
        print(message)
    return count
