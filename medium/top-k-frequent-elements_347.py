# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.


# Example 1:

# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
# Example 2:

# Input: nums = [1], k = 1
# Output: [1]

# ---------------------------------------Runtime 108 ms Beats 61.29% Memory 21.4 MB Beats 11.11%---------------------------------------

from collections import Counter


from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d: Counter = Counter(nums)
        arr: list[tuple] = sorted(
            list(zip(d.keys(), d.values())), key=lambda x: x[1] * -1
        )
        return list(map(lambda x: x[0], arr))[:k]
