def sequential_search(num_list, n):
    found = False
    for i in num_list:
        if i == n:
            found = True
            break
    return found


result = sequential_search(range(0, 20), 56)
if result:
    print("Found")
else:
    print("not found")
