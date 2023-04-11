import re

# s = '[808,92][944,250]'
#
# print('s contains a =', s.__contains__('808'))
# print('s contains A =', s.__contains__('92'))
# print('s contains X =', s.__contains__('250'))
#
# list_of_coordinates = re.findall(r'\d+', s)
# X = list_of_coordinates.pop(0)
# Y = list_of_coordinates.pop(0)
# print(X, Y)

# X = 'g1eeks4geeks5'
# res = re.sub('\D', '', X)
# print(res)

Y = 'GeeksforGeeks: A computer science portal for geeks'
out = re.search('portal', Y)
# print(out.group())  # this will print the matched string
# print(out)  # this will print matched object
# print(out.span()) # this will print the range of this string
outt = re.match('portal', Y)
print(outt)

