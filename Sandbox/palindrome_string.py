def pal(str):
    print(len(str))
    if str == str[::-1]:
        return True


str = input("Enter paindrome string ")
if pal(str):
    print("Given string is palindrome")
else:
    print("Nope, Sorry !")
