#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        sentence[0] = None

    n = len(sentence)
    first = sentence[0]
    tuple_a = (n, first)
    return tuple_a
