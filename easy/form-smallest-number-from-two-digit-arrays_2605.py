# Given two arrays of unique digits nums1 and nums2, return the smallest number that contains at least one digit from each array.


# Example 1:

# Input: nums1 = [4,1,3], nums2 = [5,7]
# Output: 15
# Explanation: The number 15 contains the digit 1 from nums1 and the digit 5 from nums2. It can be proven that 15 is the smallest number we can have.
# Example 2:

# Input: nums1 = [3,5,2,6], nums2 = [3,1,7]
# Output: 3
# Explanation: The number 3 contains the digit 3 which exists in both arrays.


# ---------------------------------------Runtime 35 ms Beats 88.4% Memory 13.9 MB Beats 100%---------------------------------------

# my Solution
from typing import List


class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        l1, l2 = set(nums1), set(nums2)
        l1_min = min(l1)
        l2_min = min(l2)
        if l1 & l2:
            return min(l1 & l2)
        if l1_min > l2_min:
            l1_min, l2_min = l2_min, l1_min
        return int(f"{l1_min}{l2_min}")


# Solution rock
def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
    s1, s2 = set(nums1), set(nums2)
    if s1 & s2:
        return min(s1 & s2)
    a, b = min(nums1), min(nums2)
    return min(a, b) * 10 + max(a, b)


sol = Solution()
nums1 = [4, 1, 3]
nums2 = [5, 7]
print(sol.minNumber(nums1, nums2))
