
# S1 = "A2B2C3"
# S2 = ''
# for i in range(len(S1)):
#     if S1[i].isdigit():
#         S2 = S2 + S1[i-1]*(int(S1[i])+1)   # blank + S1[0]*(S[1]+1) , i,e , A*(2+1) = A*3
# print(S2)




S1 = [4,6,8,2,9]
print()
S2 = S1[0]
for i in range(len(S1)):
    if S1[i] > S2:
        S2 = S1[i]
#print(S2)
print(sorted(S1)[-2])     # second_largest item in the list


#https://www.geeksforgeeks.org/python-program-to-find-second-largest-number-in-a-list/




