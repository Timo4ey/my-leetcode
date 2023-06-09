# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Note that you must do this in-place without making a copy of the array.

# Example 1:

# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]
# Example 2:


# Input: nums = [0]
# Output: [0]
# ---------------------------------------Runtime 183 ms Beats 31.9% Memory 17.9 MB Beats 12.54%---------------------------------------
class List(list):
    pass


# My solution
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        if sum(nums) == 0:
            return nums
        l, r, length = 0, 1, len(nums) - 1
        while r <= length:
            if nums[l] == 0:
                nums.append(nums.pop(l))
            else:
                l += 1
            r += 1
