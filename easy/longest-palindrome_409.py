# Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.

# Letters are case sensitive, for example, "Aa" is not considered a palindrome here.

# Example 1:

# Input: s = "abccccdd"
# Output: 7
# Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.
# Example 2:

# Input: s = "a"
# Output: 1
# Explanation: The longest palindrome that can be built is "a", whose length is 1.


# ---------------------------------------Runtime 47 ms Beats 15.19% Memory 14 MB Beats 100%---------------------------------------

# 409. Longest Palindrome

# MY solution


class Solution:
    def longestPalindrome(self, s: str) -> int:
        temp_dict = {}
        perform_dict = {}
        for x in s:
            if not temp_dict.get(x):
                temp_dict[x] = 1
            elif temp_dict.get(x) and not perform_dict.get(x):
                del temp_dict[x]
                perform_dict[x] = 2
            elif temp_dict.get(x) and perform_dict.get(x):
                del temp_dict[x]
                perform_dict[x] += 2
        output = sum(perform_dict.values())
        if temp_dict:
            return output + 1
        return output


# Solution from Editorial
#
import collections


class Solution:
    def longestPalindrome(self, s):
        ans = 0
        for v in collections.Counter(s).itervalues():
            ans += v / 2 * 2
            if ans % 2 == 0 and v % 2 == 1:
                ans += 1
        return ans
