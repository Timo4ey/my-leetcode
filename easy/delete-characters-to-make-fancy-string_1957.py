# A fancy string is a string where no three consecutive characters are equal.

# Given a string s, delete the minimum possible number of characters from s to make it fancy.

# Return the final string after the deletion. It can be shown that the answer will always be unique.


# Example 1:

# Input: s = "leeetcode"
# Output: "leetcode"
# Explanation:
# Remove an 'e' from the first group of 'e's to create "leetcode".
# No three consecutive characters are equal, so return "leetcode".
# Example 2:

# Input: s = "aaabaaaa"
# Output: "aabaa"
# Explanation:
# Remove an 'a' from the first group of 'a's to create "aabaaaa".
# Remove two 'a's from the second group of 'a's to create "aabaa".
# No three consecutive characters are equal, so return "aabaa".
# Example 3:

# Input: s = "aab"
# Output: "aab"
# Explanation: No three consecutive characters are equal, so return "aab".
# ---------------------------------------Runtime 958 ms Beats 17.59% Memory 18.6 MB Beats 36.48%---------------------------------------


# Solution O(n)
class Solution:
    def makeFancyString(self, s: str) -> str:
        letters: list = []
        length: int = len(s)
        for i in range(0, length):
            if letters and (i + 1 < length) and (s[i - 1] == s[i] == s[i + 1]):
                continue
            else:
                letters.append(s[i])
        return "".join(letters)
