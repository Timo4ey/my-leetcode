# Given two strings s and t, determine if they are isomorphic.

# Two strings s and t are isomorphic if the characters in s can be replaced to get t.

# All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

# Example 1:

# Input: s = "egg", t = "add"
# Output: true
# Example 2:

# Input: s = "foo", t = "bar"
# Output: false
# Example 3:

# Input: s = "paper", t = "title"
# Output: true


# https://leetcode.com/problems/isomorphic-strings/
# My solution

# ---------------------------------------Runtime  47 ms Beats 53.81% Memory 14.2 MB Beats 100%---------------------------------------


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(set(s)) != len(set(t)):
            return False
        temp_dict = {}
        for i in range(len(s)):
            if s[i] not in temp_dict and t[i] not in temp_dict.values():
                temp_dict[s[i]] = t[i]
            elif s[i] not in temp_dict and t[i] in temp_dict.values():
                return False
            elif s[i] in temp_dict and temp_dict[s[i]] != t[i]:
                return False
        return True


# NeetCode's solution
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapSt, mapTs = {}, {}

        for c1, c2 in zip(s, t):
            if (c1 in mapSt and mapSt[c1] != c2) or (
                c2 in mapTs and mapTs[c2] != c1
            ):
                return False
            mapSt[c1] = c2
            mapTs[c2] = c1
        return True


if __name__ == "__main__":
    solution = Solution()
    s = "abcdefghijklmnopqrstuvwxyzva"
    t = "abcdefghijklmnopqrstuvwxyzck"
    s = "bbbaaaba"
    t = "aaabbbba"  # false
    # s = "aba"
    # t ="aab" # false
    print(solution.isIsomorphic(s, t))


# class Solution:
#     def isIsomorphic(self, s: str, t: str) -> bool:
#         if len(s) != len(t):
#             return False
#         set_1 = set(s)
#         set_2 = set(t)
#         if len(set_1) == len(set_2):
#             return True
#         return False


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        for i in range(1, len(s)):
            if s[i - 1] == s[i] and t[i - 1] != t[i]:
                return False
            elif s[i - 1] != s[i] and t[i - 1] == t[i]:
                return False
            else:
                continue
        return True
