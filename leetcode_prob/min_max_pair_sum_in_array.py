from typing import List

nums = [3,5,2,3]


def max_min(nums: List[int]) -> int:
    nums.sort()
    max_pair_sum = 0
    low = 0
    high = len(nums) - 1

    while low < high:
        pair_sum = nums[low] + nums[high]
        max_pair_sum = max(pair_sum, max_pair_sum)

        low += 1
        high -= 1

    return max_pair_sum


result = max_min(nums)
print(result)
