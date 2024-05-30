# You are given 2 integer arrays nums1 and nums2 of lengths n and m respectively. You are also given a positive integer k.

# A pair (i, j) is called good if nums1[i] is divisible by nums2[j] * k (0 <= i <= n - 1, 0 <= j <= m - 1).

# Return the total number of good pairs.

# Example 1:

# Input: nums1 = [1,3,4], nums2 = [1,3,4], k = 1

# Output: 5

# Explanation:

# The 5 good pairs are (0, 0), (1, 0), (1, 1), (2, 0), and (2, 2).
# Example 2:

# Input: nums1 = [1,2,4,12], nums2 = [2,4], k = 3

# Output: 2

# Explanation:

# The 2 good pairs are (3, 0) and (3, 1).


# Constraints:

# 1 <= n, m <= 50
# 1 <= nums1[i], nums2[j] <= 50
# 1 <= k <= 50

# ---------------------------------------Runtime 56 ms Beats 38.76% Memory 16.60 MB Beats 17.90%---------------------------------------

from collections import defaultdict
from typing import Dict, List


class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        res = 0
        s: Dict[int, int] = defaultdict(int)

        for n2 in nums2:
            s[n2 * k] = s.get(n2 * k, 0) + 1

        for n1 in nums1:
            for mod, count in s.items():
                res += n1 % mod == 0 and count or 0

        return res
