# l1 = [0,2,4,1,4,0,5,0,7]
# n = len(l1)
# c = l1.count(0)
# actual_len = n-c
# print(actual_len)
# for i in range(actual_len):
#     if l1[i] == 0:
#         l1.append(l1[i])
#         c+=1
#         l1.remove(l1[i])
# print(l1)
# # l1.reverse()
# # print(l1)

#
# # easy solution for appending it to the beginning
# def move_zeros_to_beginning(l1):
#     # Initialize an index to keep track of the position where next zero should be placed
#     zero_index = 0
#
#     # Iterate through the list
#     for i in range(len(l1)):
#         # If the element is zero, swap it with the element at zero_index
#         if l1[i] == 0:
#             l1[i], l1[zero_index] = l1[zero_index], l1[i]
#             # Increment zero_index to the next position
#             zero_index += 1
#
#     return l1
#
#
# # Test the function
# l1 = [0, 2, 4, 1, 4, 0, 5, 0, 7]
# move_zeros_to_beginning(l1)
# print(l1)


def move_zeros_to_beginning(l1):
    # Initialize an index to keep track of the position where next non-zero element should be placed
    non_zero_index = len(l1) - 1

    # Iterate through the list in reverse order
    for i in range(len(l1) - 1, -1, -1):
        # If the element is non-zero, swap it with the element at non_zero_index
        if l1[i] != 0:
            l1[i], l1[non_zero_index] = l1[non_zero_index], l1[i]
            # Decrement non_zero_index to the previous position
            non_zero_index -= 1

    return l1

# Test the function
l1 = [0, 2, 4, 1, 4, 0, 5, 0, 7]
move_zeros_to_beginning(l1)
print(l1)
