#!/usr/bin/python3
def safe_print_division(a, b):
    y = None
    try:
        y = a / b
        return y
    except ZeroDivisionError:
       # print("Inside result: {}".format(None))
        return None
    finally:
        print("Inside result: {}".format(y)) 
