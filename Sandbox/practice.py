my_wieght = float(input("Enter your weight" ))

Temp = input("Is your weight in Kgs or Lbs ? " )

if Temp == 'l':
    my_wieght = my_wieght*0.453
    print("Then, Your wieight in Kg's", my_wieght)
elif Temp == 'k':
    my_wieght = my_wieght*2.2
    print("Then, Your wieight in Pounds", my_wieght)