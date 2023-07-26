#!/usr/bin/python3

def no_c(my_string):
    """removes all c and C in string"""
    string = []
    for index in range(0, len(my_string)):
        if "c" == my_string[index] or "C" == my_string[index]:
            continue
        else:
            string.append(my_string[index])

    return("".join(string))
