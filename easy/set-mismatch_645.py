# You have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set, which results in repetition of one number and loss of another number.

# You are given an integer array nums representing the data status of this set after the error.

# Find the number that occurs twice and the number that is missing and return them in the form of an array.

# Example 1:

# Input: nums = [1,2,2,4]
# Output: [2,3]
# Example 2:

# Input: nums = [1,1]
# Output: [1,2]


# Constraints:

# 2 <= nums.length <= 104
# 1 <= nums[i] <= 104

# ---------------------------------------Runtime 145 ms Beats 97.59% Memory 18.88 MB Beats 37.76%---------------------------------------

from typing import List


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        nums_set = set(nums)
        seen = set()

        global error
        error = 0
        for i in nums:
            if i in seen:
                error = i
                break
            seen.add(i)

        m = max(nums)

        for i in range(1, m + 2):
            if i not in nums_set:
                return error, i
