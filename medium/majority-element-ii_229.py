# Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

# Example 1:

# Input: nums = [3,2,3]
# Output: [3]
# Example 2:

# Input: nums = [1]
# Output: [1]
# Example 3:

# Input: nums = [1,2]
# Output: [1,2]

# ---------------------------------------Runtime 111 ms Beats 57.15% Memory 17.5 MB Beats 99.79%---------------------------------------
from collections import Counter
from typing import List


# Time complexity O(n)
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        n = len(nums) / 3
        return list(filter(lambda key: count[key] > n, count.keys()))
