import os
# import sys
#
#
# print(os.getcwd())
#
# print(os.chdir('/Users/hakumar/PycharmProjects/Experiments/BrowserFramework/Screenshots'))
#
# print(os.getcwd())
#
# ###################
# directory = os.path.dirname(os.path.abspath(__file__))
# print(directory)
#
# filename = "touch os_test.txt"
# filepath = os.path.join(directory, filename)
#
# cmd = 'touch a_filename.txt'
# os.system(cmd)
#
# print(filepath)
# with open(filepath, 'w') as file:
#     file.write("")


result = os.scandir()
for x in result:
    print(x)

