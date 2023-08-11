#!/usr/bin/python3
if __name__ == "__main__":

    import sys
    n = len(sys.argv)
    n = n - 1
    if n == 0:
        print("{} arguments.".format(n))
    elif n > 1:
        print("{} arguments:".format(n))
    else:
        print("{} argument:".format(n))
    i = 0
    for args in sys.argv[1:]:
        i = i+1
        print("{}: {}".format(i, args))
