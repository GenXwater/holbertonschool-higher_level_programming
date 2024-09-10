#!/usr/bin/python3

# variante solution :
# new_list = [replace if item == search else item for item in my_list]
#    return new_list

def search_replace(my_list, search, replace):
    new_list = my_list[:]
    for n in range(len(new_list)):
        if new_list[n] == search:
            new_list[n] = replace
    return new_list
