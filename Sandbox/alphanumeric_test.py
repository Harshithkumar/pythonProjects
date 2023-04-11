p1 = input("Enter alpanumeric string   ")

alphabets = []
digits = []

for i in p1:
    if i.isalpha():
        alphabets += i
    else:
        digits += i

alphadigits = ''
print("Before sorting ->  ", alphabets)
print(sorted(alphabets))
print("Before sorting digits->  ", digits)
print(sorted(digits))

alphasorted = sorted(alphabets) + sorted(digits)
print('Eg1=', alphasorted)
alpastr = ''.join(alphasorted)
S3 = set(alpastr)



# print("eg", reversed(sorted(alphasorted))) # this wont work
print("Sorted in the list format", sorted(alphabets + digits))
print("Sorted in the string format", ''.join(sorted(alphabets + digits)))
print("Sorted in alpa first followed  by num in string format  ->  ", alpastr)
print("Removing duplicates from the sorted alphasorted -> ", ''.join(sorted(S3)))
