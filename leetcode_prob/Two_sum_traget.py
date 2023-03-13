s = [2,7,11,15,1,4,5]

target = int(input("Enter the numbers in the above list so that it sum of 2 numbers " ,))
seen = set()

for i in s:
    needed = target - i
    if needed in seen:
        k = s.index(needed)
        j = s.index(i)
        print(f' Position of the numbers which are responsible for the sum are {k}  and  {j}')
        print(f' Actual Numbers which are responsible for the sum are {s[k]}  and  {s[j]}')
    seen.add(i)

