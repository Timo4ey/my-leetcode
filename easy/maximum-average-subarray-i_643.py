# You are given an integer array nums consisting of n elements,
# and an integer k.

# Find a contiguous subarray whose length is equal to k that has
# the maximum average value and return this value. Any answer with a
# calculation error less than 10-5 will be accepted.
 
# Example 1:

# Input: nums = [1,12,-5,-6,50,3], k = 4
# Output: 12.75000
# Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
# Example 2:

# Input: nums = [5], k = 1
# Output: 5.00000

# ---------------------------------------Runtime 1162 ms Beats 87.53% Memory 28.5 MB Beats 24.18%---------------------------------------

# My solution
# Time complexity O(n)
class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        window_sum: int = sum(nums[:k])
        ans: float | int = window_sum

        for i in range(len(nums) - k):
            window_sum = window_sum - nums[i] + nums[i + k]
            ans = max(window_sum, ans)
        return ans / k
