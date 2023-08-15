#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_b) > 2 or len(tuple_a) > 2:
        new_tuple_b = (tuple_b[0], tuple_b[1])
        tuple_b = new_tuple_b

    if len(tuple_a) > 2:
        new_tuple_a = (tuple_a[0], tuple_b[1])
        tuple_a = new_tuple_a

    if len(tuple_b) == 0:
        new_tuple = (0, 0)
        tuple_b = new_tuple

    if len(tuple_a) == 0:
        new_tuple = (0, 0)
        tuple_a = new_tuple

    if len(tuple_b) == 1:
        new_tuple = (tuple_b[0], 0)
        tuple_b = new_tuple

    if len(tuple_a) == 1:
        new_tuple = (tuple_b[0], 0)
        tuple_b = new_tuple

    new_tuple = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
    return new_tuple
