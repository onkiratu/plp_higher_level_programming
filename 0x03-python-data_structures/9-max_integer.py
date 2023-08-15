#!/usr/bin/python
def max_integer(my_list=[]):
    max_int = my_list[0]

    for integer in my_list:
        if integer > max_int:
            max_int = integer

    return max_int
