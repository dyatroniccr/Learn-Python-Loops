my_list = [43,23,6,87,43,1,4,6,3,67,8,3445,3,7,5435,63,346,3,456,734,6,34]

#Your code go from here:
def maxInteger(list1):
    bigger_number = 0
    for i in list1:
        if (i > bigger_number):
            bigger_number = i

    return bigger_number


print(maxInteger(my_list))