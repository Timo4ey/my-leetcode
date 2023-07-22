# Given two integer arrays nums1 and nums2, sorted in non-decreasing order, return the minimum integer common to both arrays. If there is no common integer amongst nums1 and nums2, return -1.

# Note that an integer is said to be common to nums1 and nums2 if both arrays have at least one occurrence of that integer.


# Example 1:

# Input: nums1 = [1,2,3], nums2 = [2,4]
# Output: 2
# Explanation: The smallest element common to both arrays is 2, so we return 2.
# Example 2:

# Input: nums1 = [1,2,3,6], nums2 = [2,3,4,5]
# Output: 2
# Explanation: There are two common elements in the array 2 and 3 out of which 2 is the smallest, so 2 is returned.


# ---------------------------------------Runtime 470 ms Beats 38.75% Memory 40.9 MB Beats 25.93%---------------------------------------


# Solution
# Time Complexity O(n)
from collections import defaultdict


class Solution:
    def getCommon(self, nums1: list[int], nums2: list[int]) -> int:
        nums1Set = set(nums1)
        nums2Set = set(nums2)
        return (
            -1
            if not nums1Set.intersection(nums2Set)
            else min(nums1Set.intersection(nums2Set))
        )

#@abdullayevakbar0101
# Time complexity:
# O(n∗log(n))
class Solution:
    def getCommon(self, nums1: list[int], nums2: list[int]) -> int:
        mp = defaultdict(int)
        for i in nums1:
            mp[i] = 1
        for i in nums2:
            if mp[i] == 1:
                return i
        return -1
