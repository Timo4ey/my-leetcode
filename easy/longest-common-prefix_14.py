# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".


# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
# ---------------------------------------Runtime 64 ms Beats 5.2% Memory 16.3 MB Beats 19.4%---------------------------------------


class List(list):
    pass


# My solution
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        i = el = 0
        pattern = ""
        while i <= len(strs[0]):
            i += 1
            temp_pattern = strs[0][:i]
            while el <= len(strs) - 1:
                if temp_pattern == strs[el][:i] and el == len(strs) - 1:
                    pattern = temp_pattern
                elif temp_pattern != strs[el][:i]:
                    return pattern

                el += 1
            el = 0
        return pattern


# ---------------------------------------Runtime 57 ms Beats 7.43% Memory 16.4 MB Beats 19.4%---------------------------------------


# Solution @abdullayevakbar0101
class Solution:
    def longestCommonPrefix(self, v: List[str]) -> str:
        ans = ""
        v = sorted(v)
        first = v[0]
        last = v[-1]
        for i in range(min(len(first), len(last))):
            if first[i] != last[i]:
                return ans
            ans += first[i]
        return ans
