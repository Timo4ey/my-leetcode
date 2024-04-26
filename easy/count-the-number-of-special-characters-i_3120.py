# You are given a string word. A letter is called special if it appears both in lowercase and uppercase in word.

# Return the number of special letters in word.

# Example 1:

# Input: word = "aaAbcBC"

# Output: 3

# Explanation:

# The special characters in word are 'a', 'b', and 'c'.

# Example 2:

# Input: word = "abc"

# Output: 0

# Explanation:

# No character in word appears in uppercase.

# Example 3:

# Input: word = "abBCab"

# Output: 1

# Explanation:

# The only special character in word is 'b'.

# Constraints:

# 1 <= word.length <= 50
# word consists of only lowercase and uppercase English letters.

# ---------------------------------------Runtime 29 ms Beats 93.92% Memory 16.39 MB Beats 99.39%---------------------------------------


class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        d = dict(zip(word, [1] * len(word)))
        return len([w for w in d.keys() if w.isupper() and d.get(w.lower())])
