#!/usr/bin/python3

def best_score(a_dictionary):
    biggest = float('-inf')
    key_big = None
    if a_dictionary == None:
        return None
    for key, value in a_dictionary.items():
        if isinstance(value, int) and value > biggest:
            biggest = value
            key_big = key
    return key_big

        
