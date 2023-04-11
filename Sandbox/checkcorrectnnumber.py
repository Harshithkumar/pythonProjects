import random
num = 25
guess_the_num = int(num*random.random() + 1)
guess = 0
c = 3
print("You have only 3 attempts to guess the random number !, Be careful")
while c>0:

        input_num = int(input("New Number: "))
        c = c-1
        print("You have only", c ," attempts to guess the random number !, Be careful")
        if (input_num > guess_the_num):
         print("number is too large, Here is the random number -> " )
        elif input_num < guess_the_num:
          print("number is too small. Here is the random number ->" )
        elif input_num == guess_the_num:
          print("number = ",guess_the_num, "Congrats" )