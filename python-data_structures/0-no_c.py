#!/usr/bin/python3

def no_c(my_string):
    """removes all c and C in string"""
    string = list(my_string)
    for index in string:
        if "c" == index or "C" == index:
            string.remove(index)
    return("".join(string))
