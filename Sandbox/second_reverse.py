s1 = ["Enter", "the", "string", "one", "two", "three"]
s3 = []
i = 0
while i<len(s1):
    if i % 2 == 0:
        s3.append(s1[i])
    else:
        s3.append(s1[i][::-1])
    i += 1
print(s3)