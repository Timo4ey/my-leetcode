# Given a string s, sort it in decreasing order based on the frequency of the characters. The frequency of a character is the number of times it appears in the string.

# Return the sorted string. If there are multiple answers, return any of them.

# Example 1:

# Input: s = "tree"
# Output: "eert"
# Explanation: 'e' appears twice while 'r' and 't' both appear once.
# So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
# Example 2:

# Input: s = "cccaaa"
# Output: "aaaccc"
# Explanation: Both 'c' and 'a' appear three times, so both "cccaaa" and "aaaccc" are valid answers.
# Note that "cacaca" is incorrect, as the same characters must be together.
# Example 3:

# Input: s = "Aabb"
# Output: "bbAa"
# Explanation: "bbaA" is also a valid answer, but "Aabb" is incorrect.
# Note that 'A' and 'a' are treated as two different characters.


# ---------------------------------------Runtime 40 ms Beats 98.96% Memory 17.5 MB Beats 92.95%---------------------------------------
from collections import Counter


# Time Complexity O(nLogn)
class Solution:
    def frequencySort(self, s: str) -> str:
        counter = Counter(s)
        return "".join(
            map(
                lambda x: x[0] * x[1],
                sorted(
                    counter.items(),
                    key=lambda a: a[1] * -1,
                ),
            )
        )
