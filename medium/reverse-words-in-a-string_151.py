# Given an input string s, reverse the order of the words.

# A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

# Return a string of the words in reverse order concatenated by a single space.

# Note that s may contain leading or trailing spaces or multiple spaces between two words.
# The returned string should only have a single space separating the words. Do not include any extra spaces.


# Example 1:

# Input: s = "the sky is blue"
# Output: "blue is sky the"
# Example 2:

# Input: s = "  hello world  "
# Output: "world hello"
# Explanation: Your reversed string should not contain leading or trailing spaces.
# Example 3:


# Input: s = "a good   example"
# Output: "example good a"
# Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.
# ---------------------------------------Runtime 40 ms Beats 54.80% Memory 16.4 MB Beats 40.97%---------------------------------------
class Solution:
    def reverseWords(self, s: str) -> str:
        data = s.split()
        start, end = 0, len(data) - 1
        while start < end:
            data[start], data[end] = data[end], data[start]
            start += 1
            end -= 1
        return " ".join(data)
