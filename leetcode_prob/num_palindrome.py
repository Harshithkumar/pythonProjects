x = int(input("Enter any number "))
b = 0

if x < 0 or x%10 == 0:
    print("Not a pal")
    exit()

while x > b:
    b = b*10 + x%10
    x = x // 10
c = b//10
if x == b or x == c:
    print(x, "and", c)
    print("Its pal")
else:
    print(x, "and", c)
    print("Nope")