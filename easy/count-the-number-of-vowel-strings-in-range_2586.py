# You are given a 0-indexed array of string words and two integers left and right.

# A string is called a vowel string if it starts with a vowel character and ends with a vowel character where vowel characters are 'a', 'e', 'i', 'o', and 'u'.

# Return the number of vowel strings words[i] where i belongs to the inclusive range [left, right].

# Example 1:

# Input: words = ["are","amy","u"], left = 0, right = 2
# Output: 2
# Explanation:
# - "are" is a vowel string because it starts with 'a' and ends with 'e'.
# - "amy" is not a vowel string because it does not end with a vowel.
# - "u" is a vowel string because it starts with 'u' and ends with 'u'.
# The number of vowel strings in the mentioned range is 2.
# Example 2:

# Input: words = ["hey","aeo","mu","ooo","artro"], left = 1, right = 4
# Output: 3
# Explanation:
# - "aeo" is a vowel string because it starts with 'a' and ends with 'o'.
# - "mu" is not a vowel string because it does not start with a vowel.
# - "ooo" is a vowel string because it starts with 'o' and ends with 'o'.
# - "artro" is a vowel string because it starts with 'a' and ends with 'o'.
# The number of vowel strings in the mentioned range is 3.

# ---------------------------------------Runtime 68 ms Beats 92.55% Memory 14.2 MB Beats 100%---------------------------------------


from functools import reduce
from typing import List

# My solution 1


class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        count = 0
        result = 0
        arr = words[left : right + 1]
        while count <= len(arr) - 1:
            vowel = dict(
                zip(("a", "e", "i", "o", "u"), ("a", "e", "i", "o", "u"))
            )
            if vowel.get(arr[count][0]) and vowel.get(arr[count][-1]):
                result += 1
            count += 1
        return result


# My solution 2
class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        def count_vowel(string):
            vowel = dict(
                zip(("a", "e", "i", "o", "u"), ("a", "e", "i", "o", "u"))
            )
            if vowel.get(string[0]) and vowel.get(string[-1]):
                return 1
            return 0

        return reduce(
            lambda acc, x: acc + count_vowel(x), words[left : right + 1], 0
        )


# Solution Spaulding_
class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        vowels = set("aeiou")

        return sum(
            {w[0], w[-1]}.issubset(vowels) for w in words[left : right + 1]
        )
