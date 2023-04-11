# import re
#
# name1 = 'harshithkumar'
#
# name2 = 'mar'
#
# match = re.match(name2, name1)
#
# print(match)
#
# if match:
#     print("regex matches: ", match.group())
# else:
#     print('pattern not found')
#
#
# if name2 in name1:
#     print('yes')
# else:
#     print("No")

def check_true_or_false():
    device = ""
    if device:
        print("name of the device ", device)
        return True
    else:
        print("inside else")
        return False


assert check_true_or_false(), "Not fine"
