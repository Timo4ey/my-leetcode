
# Given a list of dominoes, dominoes[i] = [a, b]
# is equivalent to dominoes[j] = [c, d] if and only
# if either (a == c and b == d), or (a == d and b == c) - that is, one domino can be rotated to be equal to another domino.

# Return the number of pairs (i, j) for which 0 <= i < j < dominoes.length, and dominoes[i] is equivalent to dominoes[j].

# Example 1:

# Input: dominoes = [[1,2],[2,1],[3,4],[5,6]]
# Output: 1
# Example 2:

# Input: dominoes = [[1,2],[1,2],[1,1],[1,2],[2,2]]
# Output: 3

# ---------------------------------------Runtime 260 ms Beats 42.28% Memory 26 MB Beats 78.32%---------------------------------------

# Time Complexity O(n)

from collections import defaultdict


class Solution:
    def numEquivDominoPairs(self, dominoes: list[list[int]]) -> int:
        ans: int = 0
        counter: defaultdict[tuple(int, int): int] = defaultdict(int)
        for v1, v2 in dominoes:
            key: tuple = min(v1, v2), max(v1, v2)
            ans += counter[key]
            counter[key] += 1
        return ans
