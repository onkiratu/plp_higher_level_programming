#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    answer = 0
    for args in sys.argv[1:]:
        answer = answer + int(args)
    print("{}".format(answer))
