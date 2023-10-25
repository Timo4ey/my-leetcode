# Given a string s, find the first non-repeating
# character in it and return its index. If it does not exist, return -1.

# Example 1:

# Input: s = "leetcode"
# Output: 0
# Example 2:

# Input: s = "loveleetcode"
# Output: 2
# Example 3:

# Input: s = "aabb"
# Output: -1

# ---------------------------------------Runtime 81 ms Beats 88% Memory 16.3 MB Beats 90.97%---------------------------------------


from collections import Counter


# Solution 1
class Solution:
    def firstUniqChar(self, s: str) -> int:
        letter_map = Counter(s)
        for index, letter in enumerate(s):
            if letter_map[letter] == 1:
                return index

        return -1


# Solution 2


class Solution:
    def firstUniqChar(self, s: str) -> int:
        letter_map = {}
        for index, letter in enumerate(s):
            if letter not in letter_map:
                letter_map[letter] = []

            letter_map[letter].append((index, letter))

        for _, value in letter_map.items():
            if len(value) == 1:
                return value[0][0]

        return -1


# Solution


class Solution:
    def firstUniqChar(self, s: str) -> int:
        letter_map = {}
        for index, letter in enumerate(s):
            if letter not in letter_map:
                letter_map[letter] = []

            letter_map[letter].append((index, letter))
        one_appears = list(
            filter(lambda x: len(letter_map[x]) == 1, letter_map)
        )
        if not one_appears:
            return -1
        return letter_map[one_appears[0]][0][0]
