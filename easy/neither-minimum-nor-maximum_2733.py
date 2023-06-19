# Given an integer array nums containing distinct positive integers,
# find and return any number from the array that is neither the minimum
# nor the maximum value in the array, or -1 if there is no such number.

# Return the selected integer.

# Example 1:

# Input: nums = [3,2,1,4]
# Output: 2
# Explanation: In this example, the minimum value is 1 and the maximum value is 4.
# Therefore, either 2 or 3 can be valid answers.
# Example 2:

# Input: nums = [1,2]
# Output: -1
# Explanation: Since there is no number in nums that is neither
# the maximum nor the minimum, we cannot select a number that satisfies the given condition. Therefore, there is no answer.
# Example 3:

# Input: nums = [2,1,3]
# Output: 2
# Explanation: Since 2 is neither the maximum nor the minimum value in nums, it is the only valid answer.

# ---------------------------------------Runtime 371 ms Beats 95.95% Memory 16.4 MB Beats 47.56%---------------------------------------

# My Solution 1
# Time Complexity O(n log n)


class Solution:
    def findNonMinOrMax(self, nums: list[int]) -> int:
        if len(nums) <= 2:
            return -1
        nums.sort()
        max_num: int = nums[-1]
        min_num: int = nums[0]
        return nums[1] if min_num != nums[1] != max_num else -1


# ---------------------------------------Runtime 382 ms Beats 80.58% Memory 16.4 MB Beats 47.56%---------------------------------------

# My Solution 2
# Time Complexity O(n)


class Solution:
    def findNonMinOrMax(self, nums: list[int]) -> int:
        if len(nums) <= 2:
            return -1
        max_num: int = 0
        min_num: int = float("inf")
        for i in nums:
            if i < min_num:
                min_num = i
            if i > max_num:
                max_num = i
        for i in nums:
            if i != max_num and i != min_num:
                return i


# ---------------------------------------Runtime 404 ms Beats 23.84% Memory 16.3 MB Beats 78.54%---------------------------------------

# My Solution 3
# Time Complexity O(n)


class Solution:
    def findNonMinOrMax(self, nums: list[int]) -> int:
        if len(nums) <= 2:
            return -1
        max_num: int = max(nums)
        min_num: int = min(nums)
        for i in nums:
            if i != max_num and i != min_num:
                return i
