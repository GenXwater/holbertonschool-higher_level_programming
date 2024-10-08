#!/usr/bin/python3

def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    dico = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    total = 0
    prevalue = 0

    for char in roman_string:
        currentvalue = dico.get(char, 0)
        if currentvalue > prevalue:
            total += currentvalue - prevalue * 2
        else:
            total += currentvalue
        prevalue = currentvalue

    return total
