S1 = 'geeksforgeeks'
#
# output = ''
#
# #one solution
# for ch in S1:
#     if ch not in output:
#         output+=ch
# print(output)


#2 solution we can use SET but order cannot be garuanteed

S2 = set(S1)
print("It will print in list format ", S2)
output = ''.join(S2)
S3 = sorted(S2)
print(" order cannot be Gaurateed, Without order - ", output)
print(" Its with ordered - ", ''.join(S3))
#
# print('data' * 3)
# print(3 * 'data')
# print('data' * '3')
