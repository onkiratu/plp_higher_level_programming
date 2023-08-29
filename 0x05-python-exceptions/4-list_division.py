#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []

    try:
        for i in range(list_length):
            try:
                x = my_list_1[i]
                y = my_list_2[i]

                if not isinstance(x, (int, float)) or not isinstance(x, (int, float)):
                    raise TypeError("Wrong Type")
                if y == 0:
                    raise ZeroDivisionError("division by 0")
                
                answer = x / y
                new_list.append(answer)
            except TypeError:
                print("Wrong Type")
            except ZeroDivisionError:
                print("division by 0")
            except IndexError:
                print("OUt of range")
    finally:
        return new_list
