#!/usr/bin/python3

for i in range(ord('a'), ord('{')):
    if chr(i) != 'q' and chr(i) != 'e':
        print("{}".format(chr(i)), end='')
