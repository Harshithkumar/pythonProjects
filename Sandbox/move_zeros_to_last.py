l1 = [0,2,4,0,5,0,7]
n = len(l1)

c = l1.count(0)
actual_len = n-c
for i in range(actual_len):
    if i == 0:
        l1.append(l1[i])
        c+=1
    if c == l1.count(0):
        break
print(l1)


