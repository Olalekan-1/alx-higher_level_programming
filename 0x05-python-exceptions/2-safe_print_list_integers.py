#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    count = 0  # Counter for the number of integers printed
    try:
        for item in my_list[:x]:
            if type(item) == int:
                print("{:d}".format(item), end="")
                count += 1
    except (TypeError, IndexError):
        raise ValueError("out of range")
    print()  # Print a new line
    return count
