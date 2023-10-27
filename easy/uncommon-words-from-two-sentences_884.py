# A sentence is a string of single-space separated words
# where each word consists only of lowercase letters.

# A word is uncommon if it appears exactly once in one
# of the sentences, and does not appear in the other sentence.

# Given two sentences s1 and s2, return a list of
# all the uncommon words. You may return the answer in any order.

# Example 1:

# Input: s1 = "this apple is sweet", s2 = "this apple is sour"
# Output: ["sweet","sour"]
# Example 2:

# Input: s1 = "apple apple", s2 = "banana"
# Output: ["banana"]

# ---------------------------------------Runtime 37 ms Beats 69.53% Memory 16.2 MB Beats 51.54%---------------------------------------


from typing import List
from collections import Counter


class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        res = dict(
            filter(
                lambda item: item[1] == 1,
                Counter(f"{s1} {s2}".split(" ")).items(),
            )
        )

        return list(res.keys())
