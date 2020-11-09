"""
Given a list of integers numbers "nums".
You need to find a sub-array with length less equal to "k", with maximal sum.
The written function should return the sum of this sub-array.
Examples:
    nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3
    result = 16
"""
from typing import List


def find_maximal_subarray_sum(nums: List[int], k: int) -> int:
    assert len(nums) >= k
    result = 0
    sum = 0
    while nums:
        for i in nums[0:k]:
            sum += i
            if sum > result:
                result = sum
        nums = nums[1:]
        sum = 0
    return result

