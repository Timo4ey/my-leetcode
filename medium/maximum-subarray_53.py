# Given an integer array nums, find the
# subarray
#  with the largest sum, and return its sum.

# Example 1:

# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: The subarray [4,-1,2,1] has the largest sum 6.
# Example 2:

# Input: nums = [1]
# Output: 1
# Explanation: The subarray [1] has the largest sum 1.
# Example 3:

# Input: nums = [5,4,-1,7,8]
# Output: 23
# Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.


# ---------------------------------------Runtime 624 ms Beats 29.64% Memory 30.4 MB Beats 87.16%---------------------------------------

from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_subArray = nums[0]
        curr_sum = 0
        for num in nums:
            if curr_sum < 0:
                curr_sum = 0

            curr_sum += num
            max_subArray = max(curr_sum, max_subArray)
        return max_subArray
