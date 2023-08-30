#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0

    sum_1 = sum(score * weight for score, weight in my_list)
    sum_2 = sum(weight for _, weight in my_list)

    return sum_1 / sum_2
