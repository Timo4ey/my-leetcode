# A string is considered beautiful if it satisfies the following conditions:

# Each of the 5 English vowels ('a', 'e', 'i', 'o', 'u') must appear at least once in it.
# The letters must be sorted in alphabetical order (i.e. all 'a's before 'e's, all 'e's before 'i's, etc.).
# For example, strings "aeiou" and "aaaaaaeiiiioou" are considered beautiful, but "uaeio", "aeoiu", and "aaaeeeooo" are not beautiful.

# Given a string word consisting of English vowels, return the length of the longest beautiful substring of word. If no such substring exists, return 0.

# A substring is a contiguous sequence of characters in a string.


# Example 1:

# Input: word = "aeiaaioaaaaeiiiiouuuooaauuaeiu"
# Output: 13
# Explanation: The longest beautiful substring in word is "aaaaeiiiiouuu" of length 13.
# Example 2:

# Input: word = "aeeeiiiioooauuuaeiou"
# Output: 5
# Explanation: The longest beautiful substring in word is "aeiou" of length 5.
# Example 3:

# Input: word = "a"
# Output: 0
# Explanation: There is no beautiful substring, so return 0.
# ---------------------------------------Runtime 493 ms Beats 79.77% Memory 25.4 MB Beats 7.51%---------------------------------------


# My solution
# Time Complexity O(n)


class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        ans: int = 0
        _hash: dict = {"a": "e", "e": "i", "i": "o", "o": "u", "u": "u"}
        left = word.find("a")
        prev: str = word[0]
        if len(set(word).intersection({"a", "e", "i", "o", "u"})) < 5:
            return ans
        if left > 0:
            prev: str = word[left]

        substring: list = list(word[left : left + 1])
        for right in range(left + 1, len(word)):
            if word[right] == prev or _hash.get(prev) == word[right]:
                substring.append(word[right])
                if substring[0] == "a" and substring[-1] == "u":
                    ans = max(ans, len(substring))
            else:
                left = right
                substring = list(word[left : right + 1])

            prev = word[right]
        return ans


# Solution @MtDeity


class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        seen = set()
        lo, longest = -1, 0
        for hi, c in enumerate(word):
            if hi > 0 and c < word[hi - 1]:
                seen = set()
                lo = hi - 1
            seen.add(c)
            if len(seen) == 5:
                longest = max(longest, hi - lo)
        return longest
