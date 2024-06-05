# Given a string array words, return an array of all characters that show up in all strings within the words (including duplicates). You may return the answer in any order.

# Example 1:

# Input: words = ["bella","label","roller"]
# Output: ["e","l","l"]
# Example 2:

# Input: words = ["cool","lock","cook"]
# Output: ["c","o"]


# Constraints:

# 1 <= words.length <= 100
# 1 <= words[i].length <= 100
# words[i] consists of lowercase English letters.

# ---------------------------------------Runtime 46 ms Beats 75.13% Memory 16.77 MB Beats 29.50%---------------------------------------


from collections import Counter
from typing import List


class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        head, *tail = words
        c_head = Counter(head)
        for t in tail:
            c_head &= Counter(t)

        res = []
        for k, v in c_head.items():
            while v:
                res.append(k)
                v -= 1
        return res
