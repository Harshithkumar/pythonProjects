# Python3 code to demonstrate working of
# Remove Dictionaries with Matching Values with K Key
# Using dictionary comprehension + list comprehension

# initializing list
test_list = [{'Gfg': 3, "is": 3, "best": 9},
             {'Gfg': 8, "is": 4, "best": 2},
             {'Gfg': 1, "is": 2, "best": 4},
             {'Gfg': 9, "is": 10, "best": 3},
             {'Gfg': 7, "is": 1, "best": 7}]

# printing original list
print("The original list is : " + str(test_list))

# initializing check dictionary list
check_list = [{'Gfg': 8, "Best": 1}, {"Best": 2, "Gfg": 7}]

# initializing Key
K = "Gfg"

temp = {sub[K] for sub in check_list}

res = [sub for sub in test_list if sub[K] not in temp]

print(str(res))
