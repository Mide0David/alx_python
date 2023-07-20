#!/usr/bin/python3
def reverse_string(string):
    strings = list(string)
    count = len(strings)
    toreturn = []
    for i in range(count - 1, -1, -1):
        toreturn.append(strings[i])
    final = "".join(toreturn)
    return final
