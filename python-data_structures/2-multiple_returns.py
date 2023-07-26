#!/usr/bin/python3

def multiple_returns(sentence):
    """returns  a tuple length and 1st char"""
    if not sentence:
        return 0, None
    return len(sentence), sentence[0]
    
