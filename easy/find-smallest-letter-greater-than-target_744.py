# You are given an array of characters letters that is sorted
# in non-decreasing order, and a character target. There are at least two different characters in letters.

# Return the smallest character in letters that
# is lexicographically greater than target. If such a character does not exist, return the first character in letters.

# Example 1:

# Input: letters = ["c","f","j"], target = "a"
# Output: "c"
# Explanation: The smallest character that is lexicographically greater than 'a' in letters is 'c'.
# Example 2:

# Input: letters = ["c","f","j"], target = "c"
# Output: "f"
# Explanation: The smallest character that is lexicographically greater than 'c' in letters is 'f'.
# Example 3:

# Input: letters = ["x","x","y","y"], target = "z"
# Output: "x"
# Explanation: There are no characters in letters that is lexicographically greater than 'z' so we return letters[0].

# ---------------------------------------Runtime 105 ms Beats 98.75% Memory 16.7 MB Beats 40.11%---------------------------------------

from typing import List


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        start, end = 0, len(letters) - 1
        greaters: set[str] = set()
        while start <= end:
            middle = (start + end) // 2
            guess = letters[middle]
            if guess > target:
                greaters.add(guess)
                end = middle - 1
            if guess <= target:
                start = middle + 1

        return greaters and min(greaters, key=lambda x: ord(x)) or letters[0]
