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
for i in range(len(s2)):
    if i%2==0:
        l1.append(s2[i][::-1])
    else:
        l1.append(s2[i])
print("reverse each string in the given inout order", l1)
print("reverse each string in the given inout order", l2.join(l1))