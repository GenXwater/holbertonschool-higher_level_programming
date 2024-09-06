#!/usr/bin/python3

import sys

add = 0

n = len(sys.argv)

for i in range(1, n):
    add += int(sys.argv[i])

print("{}".format(add))
