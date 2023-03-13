# Python code to print Second most repeated
# word in a sequence in Python
from collections import Counter


def secondFrequent(input):

    # Convert given list into dictionary
    # it's output will be like {'ccc':1,'aaa':3,'bbb':2}
    dict = Counter(input)
    print("Hello", dict)

    # Get the list of all values and sort it in ascending order
    keys = sorted(dict.keys())
    print("Keys", keys)

    value = sorted(dict.values())
    print("Values", value)

    # # Pick second largest element
    # secondLarge = value[0]
    # print("sec large", secondLarge)

    # Traverse dictionary and print key whose
    # value is equal to second large element
    print(dict.items())
    for (key, val) in dict.items():
        if val == 2:
            print(key, val)



# Driver program
if __name__ == "__main__":
    input = ['ddd', 'aaa', 'bbb', 'ccc', 'bbb', 'aaa', 'aaa', 'ccc']
    secondFrequent(input)
