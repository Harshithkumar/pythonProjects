s1 = 'hello how are you'
#print(len(s1))
#print(s1)
#print(len(s1))
print('given string:: ', s1)
s2 = s1.split()
print("Split string", s2)
print("index of how", s2.index('how'))
l1 = []
l2 = ' '
for i in s2:
        l1.append(i[::-1])
print("reverse each string in the given inout order", l1)
print("reverse each string in the given inout order",l2.join(l1))



#
# print("==============================================")
# l3 = []
# for i in s2[::-1]:
#     l3.append(i)
# print("reverse each word  in the same order as given inout order",l3)

# print("==============================================")
# #reverse a string without effecting sepcial charecters
#
# z1 = "a@bxyz&cgh&$%*d"
# z2 = list(z1)
# i=0
# j=len(z1)-1
#
# while i<j:
#     if not z2[i].isalpha():
#         i=i+1
#     elif not z2[j].isalpha():
#         j=j-1
#     else:
#         # z2[i],z2[j] = z2[j], z2[i]
#         tmp = z2[i]
#         z2[i] = z2[j]
#         z2[j] = tmp
#     i+=1
#     j-=1
# print(''.join(z2))






