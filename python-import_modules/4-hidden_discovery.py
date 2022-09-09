#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    for i in dir(hidden_4):
        # dir(module) find out the names defined in modules
        if i[0] != '_' and i[1] != '_':
            print(i)
