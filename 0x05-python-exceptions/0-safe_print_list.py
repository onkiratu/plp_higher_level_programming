#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        count = 0
        for i in my_list[:x]:
            print(end="{}".format(i))
            count += 1
        print()
    except TypeError:
        print()
    return count
