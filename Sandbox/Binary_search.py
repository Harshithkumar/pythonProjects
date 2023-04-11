import sys

list_items = [2, 3, 8, 9, 10, 15, 17, 19, 19, 19]
search_item = int(input("Enter the number which you need to search:"))


def bin_search(list_items, search_item):
    print("Inside the func bin_search")
    left_index = 0
    right_index = len(list_items) - 1
    mid_index = 0

    while left_index <= right_index:
        print("Inside the while loop 1")
        mid_index = (left_index + right_index) // 2
        mid_num = list_items[mid_index]
        print("mid  num", mid_num)
        count_index = []

        if mid_num == search_item:
            print("your element is at this index ->", list_items.index(mid_num))
            print("Inside the if conditoin 1")
            # This for loop is needed only when duplicates are present in the list to
            # to identify multilpe index position.
            for i in range(len(list_items)):
                # print(i)
                if mid_num == list_items[i]:
                    count_index.append(i)
            return print("your element is at this index ->", count_index)
        if mid_num < search_item:
            print("Inside the if conditoin 2")
            left_index = mid_index + 1
        else:
            print("Inside the else conditoin 3")
            right_index = mid_index - 1
    return -1


ret = bin_search(list_items, search_item)
if ret == -1:
    print("Not found", search_item)
