
# Given an array nums containing n distinct numbers in the range [0, n],
# return the only number in the range that is missing from the array.


# Example 1:

# Input: nums = [3,0,1]
# Output: 2
# Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3].
# 2 is the missing number in the range since it does not appear in nums.
# Example 2:

# Input: nums = [0,1]
# Output: 2
# Explanation: n = 2 since there are 2 numbers, so all numbers are in the range [0,2].
# 2 is the missing number in the range since it does not appear in nums.
# Example 3:

# Input: nums = [9,6,4,2,3,5,7,0,1]
# Output: 8
# Explanation: n = 9 since there are 9 numbers, so all numbers are in the range [0,9].
# 8 is the missing number in the range since it does not appear in nums.


# ---------------------------------------Runtime 147 ms Beats 41.42% Memory 17.7 MB Beats 19.3%---------------------------------------
#  Space complexity only O(1)
#  Runtime complexity O(n)

# My solution
class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n: int = len(nums)

        for i in range(len(nums)):
            n += i - nums[i]
        return n


# ---------------------------------------Runtime 140 ms Beats 61.90% Memory 17.6 MB Beats 41.69%---------------------------------------
# Solution @idhandeep

class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)
        total_sum = (n * (n + 1)) // 2
        array_sum = sum(nums)
        return total_sum - array_sum
