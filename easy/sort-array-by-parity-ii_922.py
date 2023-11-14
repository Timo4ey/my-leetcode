# Given an array of integers nums, half of the integers in nums are odd, and the other half are even.

# Sort the array so that whenever nums[i] is odd, i is odd, and whenever nums[i] is even, i is even.

# Return any answer array that satisfies this condition.

# Example 1:

# Input: nums = [4,2,5,7]
# Output: [4,5,2,7]
# Explanation: [4,7,2,5], [2,5,4,7], [2,7,4,5] would also have been accepted.
# Example 2:

# Input: nums = [2,3]
# Output: [2,3]


# ---------------------------------------Runtime 169 ms Beats 84.77% Memory 19 MB Beats 34.44%---------------------------------------

from typing import List


class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        even = [i for i in nums if i % 2 == 0]
        odd = [i for i in nums if i % 2 != 0]
        res = []
        for e, o in zip(even, odd):
            res.append(e)
            res.append(o)
        return res
