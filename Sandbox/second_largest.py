
# S1 = "A2B2C3"
# S2 = ''
# for i in range(len(S1)):
#     if S1[i].isdigit():
#         S2 = S2 + S1[i-1]*(int(S1[i])+1)   # blank + S1[0]*(S[1]+1) , i,e , A*(2+1) = A*3
# print(S2)


# Python program to find second largest number in a list
# list of numbers - length of
# list should be at least 2
list1 = [10, 20, 4, 45, 99]

mx = max(list1[0], list1[1])
secondmax = min(list1[0], list1[1])
n = len(list1)
for i in range(2, n):
    if list1[i] > mx:
        secondmax = mx
        mx = list1[i]
    elif list1[i] > secondmax and list1[i] != mx:
        secondmax = list1[i]
    elif mx == secondmax and list1[i] != secondmax:
        secondmax = list1[i]

print("Second highest number is : ",str(secondmax))

#print(sorted(S1)[-2])     # second_largest item in the list


#https://www.geeksforgeeks.org/python-program-to-find-second-largest-number-in-a-list/




