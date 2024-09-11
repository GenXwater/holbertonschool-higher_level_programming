#!/usr/bin/python3

def multiply_list_map(my_list=[], number=0):
    return list(map(lambda x: x * number, my_list))
#    new_list = my_list[:]
#    for n in range(len(new_list)):
#        new_list[n] = new_list[n] * number
#    return (new_list)
