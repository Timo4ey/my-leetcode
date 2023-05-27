
# Given a sorted array of distinct integers and a target value, return the index if the target is found.
# If not, return the index where it would be if it were inserted in order.

# You must write an algorithm with O(log n) runtime complexity.

# Example 1:

# Input: nums = [1,3,5,6], target = 5
# Output: 2
# Example 2:

# Input: nums = [1,3,5,6], target = 2
# Output: 1
# Example 3:

# Input: nums = [1,3,5,6], target = 7
# Output: 4


# ---------------------------------------Runtime 55 ms Beats 61.76% Memory 17.1 MB Beats 42.39%---------------------------------------

# My solution
# Complexity O(log n)
class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        start, end = 0, len(nums) - 1
        while start <= end:
            middle = (start + end) // 2
            guess = nums[middle]
            if guess == target:
                return middle
            elif guess > target:
                end = middle - 1
            elif guess < target:
                start = middle + 1
        return start
