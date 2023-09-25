#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    sum1 = 0

    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end='')
        except (TypeError, ValueError):
            pass
        else:
            sum1 = sum1 + 1

    print()
    return (sum1)
