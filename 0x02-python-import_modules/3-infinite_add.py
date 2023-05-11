#!/usr/bin/python3

if __name__ == '__main__':
    from sys import argv
    length = len(argv)
    add = 0
    if length == 1:
        add += 0
    else:
        for i in range(1, length):
            add += int(argv[i])
    print(add)
