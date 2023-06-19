# Companies
# Given a string s, find the length of the longest
# substring
#  without repeating characters.

# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

# ---------------------------------------Runtime 188 ms Beats 19.80% Memory 16.3 MB Beats 89.24%---------------------------------------


# My solution
# Time Complexity O(n^2)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = right = 0
        ans: int = 0
        for right in range(1, len(s)):
            curr_window: str = s[left:right]
            ans = max(ans, len(set(curr_window)))
            while (
                s[right] in curr_window
                and (left <= len(s) - 1)
                and (len(curr_window) != 1)
            ):
                left += 1
                curr_window = s[left:right]

        ans = max(ans, len(set(s[left : right + 1])))
        return ans


# Solution @zhanweiting
# Time complexity :O(n).
# Space complexity: O(m)


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        l = 0
        output = 0
        for r in range(len(s)):
            """
            If s[r] not in seen, we can keep increasing the window size by moving right pointer
            """
            if s[r] not in seen:
                output = max(output, r - l + 1)
                """
                There are two cases if s[r] in seen:
                case1: s[r] is inside the current window, we need to change the window by moving left pointer to seen[s[r]] + 1.
                case2: s[r] is not inside the current window, we can keep increase the window
                """
            else:
                if seen[s[r]] < l:
                    output = max(output, r - l + 1)
                else:
                    l = seen[s[r]] + 1
            seen[s[r]] = r
        return output
