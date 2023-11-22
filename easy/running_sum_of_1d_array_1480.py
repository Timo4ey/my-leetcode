# Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

# Return the running sum of nums.

# Example 1:

# Input: nums = [1,2,3,4]
# Output: [1,3,6,10]
# Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].
# Example 2:

# Input: nums = [1,1,1,1,1]
# Output: [1,2,3,4,5]
# Explanation: Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].
# Example 3:

# Input: nums = [3,1,2,10,1]
# Output: [3,4,6,16,17]


# https://leetcode.com/problems/running-sum-of-1d-array/
# My solution
# ---------------------------------------Runtime  56 ms Beats 12.23% Memory 14.1 MB Beats 100%---------------------------------------


# Time complexity O(N)

from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        output = []
        for i in range(len(nums)):
            output.append(sum(nums[: i + 1]))
        return output


if __name__ == "__main__":
    s = Solution()
    print(s.runningSum([1, 2, 3, 4]))
    print(s.runningSum([1, 1, 1, 1, 1]))
    print(s.runningSum([3, 1, 2, 10, 1]))
