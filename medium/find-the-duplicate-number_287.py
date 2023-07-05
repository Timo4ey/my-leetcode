# Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

# There is only one repeated number in nums, return this repeated number.

# You must solve the problem without modifying the array nums and uses only constant extra space.


# Example 1:

# Input: nums = [1,3,4,2,2]
# Output: 2
# Example 2:

# Input: nums = [3,1,3,4,2]
# Output: 3

# ---------------------------------------Runtime 626 ms Beats 48.20% Memory 35.2 MB Beats 9.95%---------------------------------------


# Time complexity O(n)
# Type TwoPointers
class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        left, right = 0, len(nums) - 1
        set_nums = set()

        while left <= right:
            n1 = nums[left]
            n2 = nums[right]
            if n1 == n2:
                return n1
            elif n1 in set_nums:
                return n1
            elif n2 in set_nums:
                return n2
            set_nums.add(n1)
            set_nums.add(n2)
            left += 1
            right -= 1

# Solution @newRuanXY
# A so-called O(1) space but essencially O(N) space algorithm using
# bit manipulation: use each bit of number seen as the seen array in solution 1.

class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        seen = 0
        for num in nums:
            if seen & (1 << num):
                return num
            seen |= 1 << num
