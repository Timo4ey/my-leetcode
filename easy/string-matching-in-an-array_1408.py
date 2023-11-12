# Given an array of string words, return all strings in words that is a substring of another word. You can return the answer in any order.

# A substring is a contiguous sequence of characters within a string

# Example 1:

# Input: words = ["mass","as","hero","superhero"]
# Output: ["as","hero"]
# Explanation: "as" is substring of "mass" and "hero" is substring of "superhero".
# ["hero","as"] is also a valid answer.
# Example 2:

# Input: words = ["leetcode","et","code"]
# Output: ["et","code"]
# Explanation: "et", "code" are substring of "leetcode".
# Example 3:

# Input: words = ["blue","green","bu"]
# Output: []
# Explanation: No string of words is substring of another string.

# ---------------------------------------Runtime 43 ms Beats 69.30% Memory 16.3 MB Beats 11.35%---------------------------------------


from typing import List


class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        res = []
        added = set()
        for word in words:
            for i in range(len(words)):
                if word in words[i] and word != words[i] and word not in added:
                    added.add(word)
                    res.append(word)
        return res
