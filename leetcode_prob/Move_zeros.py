S1 = [1,0,0,3,12,0,9]

prev_index = 0
for i in range(0,len(S1)):
    if S1[i] != 0:
        tmp = S1[prev_index]
        S1[prev_index] = S1[i]
        S1[i] = tmp
        prev_index = prev_index+1
print(S1)