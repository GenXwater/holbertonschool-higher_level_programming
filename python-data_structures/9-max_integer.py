#!/usr/bin/python3

def max_integer(my_list=[]):
    if my_list:
        nmax = my_list[0]
        for tempmax in my_list:
            if tempmax > nmax:
                nmax = tempmax
        return (nmax)
    return None
