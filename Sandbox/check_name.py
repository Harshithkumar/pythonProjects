import snoop
import factorial
num = int(input("Fact of: "))
print ("Always executed")

if __name__ == "factorial":
    print ("Executed when invoked directly")

else:
    print ("Executed when imported")

    factorial.fact(num)
    print(f"The factorial of {num} is {factorial.fact(num)}")