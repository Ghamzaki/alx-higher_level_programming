#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    length = len(my_list) - 1
    new_list = my_list[:]

    for i in range(length):
        if idx < 0 or idx > length:
            return (my_list)
        else:
            new_list[idx] = element
            return(new_list)
