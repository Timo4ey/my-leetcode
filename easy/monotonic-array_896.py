# An array is monotonic if it is either monotone increasing or monotone decreasing.

# An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j]. An array nums is monotone decreasing if for all i <= j, nums[i] >= nums[j].

# Given an integer array nums, return true if the given array is monotonic, or false otherwise.

# Example 1:

# Input: nums = [1,2,2,3]
# Output: true
# Example 2:

# Input: nums = [6,5,4,4]
# Output: true
# Example 3:

# Input: nums = [1,3,2]
# Output: false

# ---------------------------------------Runtime 28.67% Beats 28.67% Memory 30.5 MB Beats 83.11%---------------------------------------


from typing import List


class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        lng = len(nums)
        res: list[int] = []
        if lng > 1 and (max(nums) != min(nums)):
            x, y = nums[0], nums[-1]
            if x == y and max(map(abs, nums)) > y:
                return False

            if x < y:
                res = list(
                    filter(lambda i: nums[i] > nums[i + 1], range(lng - 1))
                )
            if x > y:
                res = list(
                    filter(lambda i: nums[i] < nums[i + 1], range(lng - 1))
                )

        return len(res) == 0
