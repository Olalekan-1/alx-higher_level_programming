#!/usr/bin/python3

if __name__ == '__main__':
    from sys import argv
    from calculator_1 import add, sub, mul, div
    length = len(argv)
# arg = argv[2]
    if length != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    arg = argv[2]
    if arg == '+':
        print("{} + {} = {}".format(int(argv[1]), int(argv[3]),
              add(int(argv[1]), int(argv[3]))))
# print(add(int(argv[1]), int(argv[3])))
    elif arg == '-':
        print("{} - {} = {}".format(int(argv[1]), int(argv[3]),
              sub(int(argv[1]), int(argv[3]))))
# print(sub(int(argv[1]), int(argv[3])))
    elif arg == '*':
        print("{} * {} = {}".format(int(argv[1]), int(argv[3]),
              mul(int(argv[1]), int(argv[3]))))
# print(mul(int(argv[1]), int(argv[3])))
    elif arg == '/':
        print("{} / {} = {}".format(int(argv[1]), int(argv[3]),
              div(int(argv[1]), int(argv[3]))))
# print(div(int(argv[1]), int(argv[3])))
    elif arg != "+-*/":
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
