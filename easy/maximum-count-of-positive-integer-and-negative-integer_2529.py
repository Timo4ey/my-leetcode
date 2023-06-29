# Given an array nums sorted in non-decreasing order,
# return the maximum between the number of positive integers and the number of negative integers.

# In other words, if the number of positive integers
# in nums is pos and the number of negative integers is neg, then return the maximum of pos and neg.
# Note that 0 is neither positive nor negative.

# Example 1:

# Input: nums = [-2,-1,-1,1,2,3]
# Output: 3
# Explanation: There are 3 positive integers and 3 negative integers. The maximum count among them is 3.
# Example 2:

# Input: nums = [-3,-2,-1,0,0,1,2]
# Output: 3
# Explanation: There are 2 positive integers and 3 negative integers. The maximum count among them is 3.
# Example 3:

# Input: nums = [5,20,66,1314]
# Output: 4
# Explanation: There are 4 positive integers and 0 negative integers. The maximum count among them is 4.


from ast import List
from bisect import bisect_left, bisect_right

# ---------------------------------------Runtime 134 ms Beats 79.15% Memory 16.5 MB Beats 99.65%---------------------------------------


# Solution #1 Best
# time Complexity O(log(n))
class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        neg: int = bisect_left(nums, 0)
        pos: int = len(nums) - bisect_right(nums, 0)
        return max(neg, pos)


# ---------------------------------------Runtime 141 ms Beats 45.45% Memory 16.6 MB Beats 88.88%---------------------------------------


# Solution #2
# time Complexity O(log(n))
class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        neg: int = 0
        pos: int = 0
        start, end = 0, len(nums) - 1

        while start <= end and nums[start] < 0:
            neg += 1
            start += 1

        while nums[end] > 0 and end >= start:
            pos += 1
            end -= 1

        return max(pos, neg)
