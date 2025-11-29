# s1 = 'DURGASOFTWAREi'
#
# vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
#
# count = {}
#
# for ch in s1:
#     if ch in vowels:
#         count[ch] = count.get(ch, 0) + 1
#
# print(count)  # this will be print in unsorted way
#
# print(sorted(count.items()))  ## this will be print in sorted way
#
# for k, v in sorted(count.items()):
#     print('{} occurs {} times'.format(k, v))
from collections import Counter


# def find_dup(nums):
#     dup = []
#     seen = set()
#     for num in nums:
#         if num in seen:
#             dup.append(num)
#         else:
#             seen.add(num)
#     return dup
#
#
# num_in = [2, 3, 4, 7, 2, 3, 1, 9]
# result = find_dup(num_in)
# print(result)


# def first_unique_char(s):
#     char_count = Counter(s)
#     for i, char in enumerate(s):
#         if char_count[char] == 1:
#             return i
#     return -1
#
# # Example usage
# s = "lcode"
# print(first_unique_char(s))

def two_sum(nums, target):
    lookup = {}
    for i, num in enumerate(nums):
        complement = target - num
        print(complement)
        if complement in lookup:
            print([lookup[complement], i])
            return [lookup[complement], i]
        lookup[num] = i
    return []


nums = [11, 15, 7, 2]
target = 9
print(two_sum(nums, target))
