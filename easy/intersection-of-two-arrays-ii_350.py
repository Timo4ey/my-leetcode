# Given two integer arrays nums1 and nums2, return an array of their intersection.
# Each element in the result must appear as many times as it shows in both
# arrays and you may return the result in any order.


# Example 1:

# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2,2]
# Example 2:

# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [4,9]
# Explanation: [9,4] is also accepted.

# ---------------------------------------Runtime 58 ms Beats 59.93% Memory 16.4 MB Beats 54.43%---------------------------------------

# My solution
# Time complexity O(m)
from collections import Counter


class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        counter = Counter(nums1) & Counter(nums2)
        ans = []
        for k, v in counter.items():
            ans.extend([k] * v)
        return ans
