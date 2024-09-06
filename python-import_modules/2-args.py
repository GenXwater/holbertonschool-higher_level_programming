#!/usr/bin/python3

import sys

if __name__ == '__main__':

    n = len(sys.argv)-1


    if len(sys.argv) <= 1:
        print("{} arguments.".format(n))

    elif len(sys.argv) == 2:
        print("{} argument:\n{}: {}".format(n, n, sys.argv[1]))

    else:
        print("{} arguments:".format(n))
        i = 1
        while i <= n:
            print("{}: {}".format(i, sys.argv[i]))
            i += 1
