#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = list(my_list)
    size = len(new_list)

    for i in range(size):
        if new_list[i] == search:
            new_list[i] = replace
    return new_list
