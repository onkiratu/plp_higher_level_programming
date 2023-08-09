#!/usr/bin/python3
def uppercase(str):
    for i in str:
        #PRINTING UPPERCASE
        if (ord(i) >= 65 and ord(i) <= 90) or (i >= "0" and i <= "9") or (i == " ") or (i == '\n'):
            num = ord(i)
            print(end=chr(num))
        else:
            #CHANGING LOWERCASE TO UPPERCAS
            num = ord(i) - 32
            num = chr(num)
            print(end=num)
