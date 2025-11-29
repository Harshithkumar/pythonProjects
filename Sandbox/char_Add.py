# s1 = 'a'
#
# s2 = 4
#
# print("acsii value of alphabet of a =",  ord(s1))
#
# print(chr(ord(s1)+s2))
from collections import Counter


def length_of_longest_substring(s):
    char_index = {}
    char_count = Counter(s)
    print(char_count)
    for i, j in enumerate(s):
        print(i, j)


s = "abcabcbb"
print(length_of_longest_substring(s))
