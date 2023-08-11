#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":
    names_to_print = dir(hidden_4)
    names = sorted(name for name in names if not name.startswith("__"))
    for name in names:
        print(name)
