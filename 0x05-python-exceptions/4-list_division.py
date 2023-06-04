#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    result = []
    try:
        for i in range(list_length):
            elem1 = my_list_1[i] if i < len(my_list_1) else 0
            elem2 = my_list_2[i] if i < len(my_list_2) else 0
            result.append(elem1 / elem2)
    except TypeError:
        result.append(0)
        print("wrong type")
    except ZeroDivisionError:
        result.append(0)
        print("division by 0")
    except IndexError:
        result.append(0)
        print("out of range")
    return result

