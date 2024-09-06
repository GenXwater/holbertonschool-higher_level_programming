#!/usr/bin/python3

import sys

add = 0

n = len(sys.argv)

for i in range(n - 1):
    add += int(sys.argv[i + 1])

print("{}".format(add))
