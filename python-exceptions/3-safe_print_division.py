#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        div = a / b
    except (ValueError, ZeroDivisionError):
        div = None
    finally:
        print("Inside result: {}".format(div), end="")
    print()
    return div
