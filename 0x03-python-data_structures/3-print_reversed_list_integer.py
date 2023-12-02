#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    length = len(my_list)
    count = 0
    for i in range(length):
        count -= 1
        print("{}".format(my_list[count]))
        #print("{}".format(my_list.pop()))
