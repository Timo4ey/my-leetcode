# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.


# Example 1:

# Input: nums = [3,2,3]
# Output: 3
# Example 2:

# Input: nums = [2,2,1,1,1,2,2]
# Output: 2

# ---------------------------------------Runtime 155 ms Beats 61.33% Memory 17.9 MB MB Beats 66.92%---------------------------------------


from collections import Counter


class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        count = Counter(nums)

        return max(count, key=count.get)
