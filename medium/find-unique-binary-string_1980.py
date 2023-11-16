# Given an array of strings nums containing n unique binary strings each of length n, return a binary string of length n that does not appear in nums. If there are multiple answers, you may return any of them.

# Example 1:

# Input: nums = ["01","10"]
# Output: "11"
# Explanation: "11" does not appear in nums. "00" would also be correct.
# Example 2:

# Input: nums = ["00","01"]
# Output: "11"
# Explanation: "11" does not appear in nums. "10" would also be correct.
# Example 3:

# Input: nums = ["111","011","001"]
# Output: "101"
# Explanation: "101" does not appear in nums. "000", "010", "100", and "110" would also be correct.
# nums = ["1"]
# nums = ["0100", "0010", "0101", "0000"]

# ---------------------------------------Runtime 44 ms Beats 46.90% Memory 16.4 MB Beats 42.98%---------------------------------------

from typing import List


class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        max_len = len(nums[-1])
        real_nums = {int(num, base=2) for num in nums}
        max_num = max(real_nums) + 2

        for i in range(0, max_num):
            if i not in real_nums:
                guess = bin(i)[2:]
                return "0" * (max_len - len(guess)) + guess
