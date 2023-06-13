# Given a string s and an integer k, return the maximum number of
# vowel letters in any substring of s with length k.

# Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.


# Example 1:

# Input: s = "abciiidef", k = 3
# Output: 3
# Explanation: The substring "iii" contains 3 vowel letters.
# Example 2:

# Input: s = "aeiou", k = 2
# Output: 2
# Explanation: Any substring of length 2 contains 2 vowels.
# Example 3:

# Input: s = "leetcode", k = 3
# Output: 2
# Explanation: "lee", "eet" and "ode" contain 2 vowels.

# ---------------------------------------Runtime 176 ms Beats 73.42% Memory 18.3 MB Beats 6.39%---------------------------------------

# My Solution
# Time Complexity O(n)


class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        l_vowels: int = len(s)
        vowels: set = {"a", "e", "i", "o", "u"}
        nums_s: list = [0] * l_vowels
        for i, v in enumerate(s):
            if v in vowels:
                nums_s[i] += 1

        cur_window: int = sum(nums_s[:k])
        max_n_vowels: int = cur_window
        for i in range(l_vowels - k):
            cur_window = cur_window - nums_s[i] + nums_s[i + k]
            max_n_vowels = max(cur_window, max_n_vowels)

        return max_n_vowels
