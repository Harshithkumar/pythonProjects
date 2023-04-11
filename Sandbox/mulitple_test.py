import secrets

# def multiply(*list):
#     var = 1
#     for x in list:
#         var = var * x
#     return var
#
# print("Start")
# print(multiply(2,3,5))
# print("End")

l1 = ['kolte', 'ram', 'kam', 'work', 'jim', 'shy']

def ranchoice():
    l2 = secrets.choice(l1)
    print(l2)


ranchoice()


