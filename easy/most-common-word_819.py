# Given a string paragraph and a string array of the banned words banned, return the most frequent word that is not banned. It is guaranteed there is at least one word that is not banned, and that the answer is unique.

# The words in paragraph are case-insensitive and the answer should be returned in lowercase.


# Example 1:

# Input: paragraph = "Bob hit a ball, the hit BALL flew far after it was hit.", banned = ["hit"]
# Output: "ball"
# Explanation:
# "hit" occurs 3 times, but it is a banned word.
# "ball" occurs twice (and no other word does), so it is the most frequent non-banned word in the paragraph.
# Note that words in the paragraph are not case sensitive,
# that punctuation is ignored (even if adjacent to words, such as "ball,"),
# and that "hit" isn't the answer even though it occurs more because it is banned.
# Example 2:

# Input: paragraph = "a.", banned = []
# Output: "a"

# ---------------------------------------Runtime 42 ms Beats 62.49% Memory 16.2 MB Beats 92.1%---------------------------------------


from collections import Counter
from typing import List
import re


# Time complexity O(n)
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        set_banned = set(banned)
        words = [
            word.lower()
            for word in re.findall(r"\w+", paragraph)
            if word.lower() not in set_banned
        ]
        counter = Counter(words)
        return max(counter, key=counter.get)
