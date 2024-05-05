# A word is considered valid if:

# It contains a minimum of 3 characters.
# It consists of the digits 0-9, and the uppercase and lowercase English letters. (Not necessary to have all of them.)
# It includes at least one vowel.
# It includes at least one consonant.
# You are given a string word.

# Return true if word is valid, otherwise, return false.

# Notes:

# 'a', 'e', 'i', 'o', 'u', and their uppercases are vowels.
# A consonant is an English letter that is not a vowel.


# Example 1:

# Input: word = "234Adas"

# Output: true

# Explanation:

# This word satisfies the conditions.

# Example 2:

# Input: word = "b3"

# Output: false

# Explanation:

# The length of this word is fewer than 3, and does not have a vowel.

# Example 3:

# Input: word = "a3$e"

# Output: false

# Explanation:

# This word contains a '$' character and does not have a consonant.

# Constraints:

# 1 <= word.length <= 20
# word consists of English uppercase and lowercase letters, digits, '@', '#', and '$'.

# ---------------------------------------Runtime 34 ms Beats 100.00% Memory 16.63 MB Beats 100.00%---------------------------------------


class Solution:
    def isValid(self, word: str) -> bool:
        any_symbol = [x for x in word if not x.isalpha() and not x.isdigit()]
        if not any_symbol:
            vowel = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
            N = len(word)
            dig = [i for i in word if i.isdigit()]
            alpha_up = [a for a in word if a.isupper()]
            alpha_down = [a for a in word if a.islower()]
            has_vowel = [a for a in word if a in vowel]
            constant = [a for a in word if a not in vowel and not a.isdigit()]
            if N >= 3 and constant and has_vowel:
                if dig or alpha_down or alpha_up:
                    return True
                return False

        return False
