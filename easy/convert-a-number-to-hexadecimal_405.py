# Given an integer num, return a string representing its hexadecimal representation. For negative integers, two’s complement method is used.

# All the letters in the answer string should be lowercase characters, and there should not be any leading zeros in the answer except for the zero itself.

# Note: You are not allowed to use any built-in library method to directly solve this problem.

# Example 1:

# Input: num = 26
# Output: "1a"
# Example 2:

# Input: num = -1
# Output: "ffffffff"


# Constraints:

# -231 <= num <= 231 - 1

# ---------------------------------------Runtime 36 ms Beats 48.79% Memory 16.42 MB Beats 94.15%---------------------------------------


from typing import Dict


class Solution:

    map: Dict[int, str] = {
        0: "0",
        1: "1",
        2: "2",
        3: "3",
        4: "4",
        5: "5",
        6: "6",
        7: "7",
        8: "8",
        9: "9",
        10: "a",
        11: "b",
        12: "c",
        13: "d",
        14: "e",
        15: "f",
    }

    def toHex(self, num: int) -> str:
        res = ""
        if not num:
            res = self.map[num]
        while num and len(res) <= 7:
            num, r = divmod(num, 16)
            res = f"{self.map[r]}{res}"

        return res
