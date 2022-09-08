#!/usr/bin/python3
if __name__ == "__main__":
    # This guard wont run the program when imported
    from add_0 import add
    a = 1
    b = 2
    print("{} + {} = {}".format(a, b, add(a, b)))
