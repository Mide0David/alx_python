#!/usr/bin/python3

def fibonacci_sequence(n):
    lists = []
    if n <= 0:
        return lists
    elif n == 1:
        lists.append(0)
        return lists
    else:
        lists = [0, 1]
        for i in range(2, n):
            lists.append(lists[i - 2] + lists[i - 1])
        return(lists)
