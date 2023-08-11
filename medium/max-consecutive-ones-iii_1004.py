# Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.


# Example 1:

# Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
# Output: 6
# Explanation: [1,1,1,0,0,1,1,1,1,1,1]
# Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
# Example 2:

# Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
# Output: 10
# Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
# Bolded numbers were flipped from 0 to 1. The longest subarray is underlined

# ---------------------------------------Runtime 477 ms Beats 93.57% Memory 16.9 MB Beats 97.84%---------------------------------------

# 
# Time complexity O(n)

class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        point2 = 0

        for point1 in range(len(nums)):
            if nums[point1] == 0:
                k -= 1

            if k < 0:
                if nums[point2] == 0:
                    k += 1
                point2 += 1

        return (point1 + 1) - point2
