#!/usr/bin/python3
def roman_to_int(roman_string):
    r_dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    if isinstance(roman_string, str) is False:
        return 0
    for i in roman_string:
        if i not in r_dic:
            return 0
    n = r_dic[roman_string[0]]
    for i in range(1, len(roman_string)):
        n = n + r_dic[roman_string[i]]
        if r_dic[roman_string[i - 1]] < r_dic[roman_string[i]]:
            n = n - 2 * r_dic[roman_string[i - 1]]
    return n
