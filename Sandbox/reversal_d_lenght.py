# Input:  arr[] = [1, 2, 3, 4, 5, 6, 7]
#          d = 2
# Output: arr[] = [3, 4, 5, 6, 7, 1, 2]

given_input = [1, 2, 3, 4, 5, 6, 7]
d_len = 2
arr_len = len(given_input)


def rotate_array(op_arr, d_len, arr_len):
    out_arr = op_arr[d_len:] + op_arr[:d_len]
    return out_arr


result = rotate_array(given_input, d_len, arr_len)
print(result)
