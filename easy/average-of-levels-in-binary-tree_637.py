# Given the root of a binary tree, return the average value of the nodes on each level in the form of an array.
# Answers within 10-5 of the actual answer will be accepted.

# Example 1:

# Input: root = [3,9,20,null,null,15,7]
# Output: [3.00000,14.50000,11.00000]
# Explanation: The average value of nodes on level 0 is 3, on level 1 is 14.5, and on level 2 is 11.
# Hence return [3, 14.5, 11].
# Example 2:

# Input: root = [3,9,20,15,7]
# Output: [3.00000,14.50000,11.00000]


# Constraints:

# The number of nodes in the tree is in the range [1, 104].
# -231 <= Node.val <= 231 - 1

# ---------------------------------------Runtime 48 ms Beats 83.6% Memory 19.7 MB Beats 6.87%---------------------------------------

from collections import defaultdict
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        levels: defaultdict[int, list] = defaultdict(int)

        def dfs(node: TreeNode | None, step: int = 1):
            if node:
                if step not in levels:
                    levels[step] = []
                levels[step].append(node.val)
                dfs(node.left, step=step + 1)
                dfs(node.right, step=step + 1)

        dfs(root)

        return list(
            map(lambda key: sum(levels[key]) / len(levels[key]), levels)
        )
