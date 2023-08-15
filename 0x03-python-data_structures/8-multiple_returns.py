#!/usr/bin/python3
def multiple_returns(sentence):
    if not sentence:
        return 0, None

    n = len(sentence)
    first = sentence[0]
    tuple_a = (n, first)
    return tuple_a
