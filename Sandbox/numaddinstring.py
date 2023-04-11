S1 = 'AB15CD10EF15'
num = 0
sum = 0


# This is adding of given integer as a while like 15
for i in S1:
    if i.isdigit():
        print(i)
        num = num*10+int(i)    # 10 + 5 = 15
    else:
        sum = sum + num
        num = 0
print("Sum of number in String  =  " , sum+num)

# This is adding of single integer  like 1+5
number = 0
for j in S1:
    if j.isdigit():
        number = number + int(j)   # 8 + 5 = 13
print(number)