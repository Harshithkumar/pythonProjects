def pal(str):
    print(len(str))
    if str == str[::-1]:
        return True


str = 'MADAM'
if pal(str):
    print("Given string is palindrome")
else:
    print("Nope, Sorry !")
