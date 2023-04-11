# Print the number into consecutive alpha
s1 = 'a44'
s2 = ''
i = 0
c = 0

# while i < len(s1):
#     if s1[i].isalpha():
#         s2 = s2 + s1[i]
#     else:
#         print("Before S1 position =",len(s1)-i)
#         print("After S1 position = ", (i - (len(s1)-1)))
#         print("S1 value = ", s1[i - (len(s1)-1)])
#         y = ord(s1[i - (len(s1)-1)])
#         z = int(s1[i]) #int(4) = 4
#         x = y + z
#         m = chr(x)
#         s2 = s2 + m
#         print(y, z, x, m ,s2)
#     i = i + 1
#
#
# print(s2)


for i in range(len(s1)):
    if s1[i].isalpha():
         s2 = s2 + s1[i]
    else:
        y = ord(s1[0])
        z = int(s1[i])
        x = y + z
        m = chr(x)
        s2 = s2 + m
        print(y, z, x, m ,s2)
        c = len(s2)
        print("Lenght of S2 String = ", c)
print(s2)