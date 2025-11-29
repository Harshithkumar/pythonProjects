from collections import defaultdict

# initializing list
test_list = ["GFG-1", 4, 6, 7, 10, "GFG-2", 2, 3, "GFG-3", 9, 2, 4, 6]

# initializing prefix
temp = "GF"

res = defaultdict(list)

for i in test_list:
    if str(i).startswith(temp):
        key = i
    else:
        res[key].append(i)

# printing result
print("The constructed dictionary : " + str(res))
