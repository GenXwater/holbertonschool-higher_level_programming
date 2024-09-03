#!/usr/bin/python3
for alphabet in range(97, 123):
    if chr(alphabet) in ('q', 'e'):
        continue
    print("{}".format(chr(alphabet)), end="")
