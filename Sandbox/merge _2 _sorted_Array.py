
# Python3 code to demonstrate
# to combine two sorted list
# using naive method

# initializing lists
test_list1 = [1, 5, 6, 9, 11,11,12,19,20,24,25]
test_list2 = [1, 5, 7, 8, 10,18,28]

print("before testing 1 ", test_list1[7:])
print("before testing  2", test_list2[6:])


# printing original lists
print ("The original list 1 is : " + str(test_list1))
print ("The original list 2 is : " + str(test_list2))

# using naive method
# to combine two sorted lists
size_1 = len(test_list1)
size_2 = len(test_list2)

res = []
i, j = 0,0

while i < size_1 and j < size_2:
    if test_list1[i] < test_list2[j]:
        res.append(test_list1[i])
        i += 1

    else:
        res.append(test_list2[j])
        j += 1
print("i  position ",i)
print("j  position ", j)
res = res + test_list1[i:] + test_list2[j:]
print(res)


s2 = []
s2 = test_list1 + test_list2
print("adding 2 list and then sort ! Simple !!", sorted(s2))
