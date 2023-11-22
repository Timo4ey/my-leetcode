# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

# Example 1:

# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:

# Input: s = "rat", t = "car"
# Output: false

# ---------------------------------------Runtime 53 ms Beats 62.74% Memory 14.4 MB Beats 100%---------------------------------------


# My solution
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def get_dict(array):
            temp_dict = {}
            for i in array:
                if not temp_dict.get(i):
                    temp_dict[i] = 1
                else:
                    temp_dict[i] += 1
            return temp_dict

        s1 = get_dict(s)
        t1 = get_dict(t)
        return s1 == t1


# My solution 2


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def get_dict(array):
            temp_dict = {}
            for i in array:
                temp_dict[i] = temp_dict.get(i, 0) + 1
            return temp_dict

        s1 = get_dict(s)
        t1 = get_dict(t)
        return s1 == t1
