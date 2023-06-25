# Given a string s consisting only of characters a, b and c.

# Return the number of substrings containing at least one occurrence of all these characters a, b and c.


# Example 1:

# Input: s = "abcabc"
# Output: 10
# Explanation: The substrings containing at least one occurrence of the characters a, b and c are "abc", "abca", "abcab", "abcabc", "bca", "bcab", "bcabc", "cab", "cabc" and "abc" (again).
# Example 2:

# Input: s = "aaacb"
# Output: 3
# Explanation: The substrings containing at least one occurrence of the characters a, b and c are "aaacb", "aacb" and "acb".
# Example 3:

# Input: s = "abc"
# Output: 1

# ---------------------------------------Runtime 236 ms Beats 62.74% Memory 16.7 MB Beats 84.58%---------------------------------------


# Time Complexity O(n)
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        left: int = 0
        ans: int = 0

        curr_window: dict = {x: 0 for x in s}

        # count appearance of letters
        for i in s:
            curr_window[i] += 1
            # if cur_window has at leat one of each letter abc we count any
            # substraction
            while (
                curr_window.get("a")
                and curr_window.get("b")
                and curr_window.get("c")
            ):
                curr_window[s[left]] -= 1
                left += 1
            ans += left

        return ans
