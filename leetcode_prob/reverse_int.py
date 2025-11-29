def reverse_num(x):
    int_min , int_max = -2**31, 2**31-1

    #determine if x is -ve
    num_sign = -1 if x < 0 else 1
    x *= num_sign

    #reverse a given integer
    reversed_x = int(str(x)[::-1]) * num_sign

    if reversed_x < int_min or reversed_x > int_max:
        return 0
    return reversed_x

print(reverse_num(-123))
