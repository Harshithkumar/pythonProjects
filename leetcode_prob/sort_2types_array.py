arr = [1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0]

i = 0
j = len(arr)-1

while i < j:
    if arr[j] == 1:
        j = j - 1
    else:
        tmp = arr[i]
        arr[i] = arr[j]
        arr[j] = tmp
        i = i + 1

print(arr)