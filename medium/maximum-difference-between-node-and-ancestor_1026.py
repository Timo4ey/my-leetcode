# Given the root of a binary tree, find the maximum value v for which there exist different nodes a and b where v = |a.val - b.val| and a is an ancestor of b.

# A node a is an ancestor of b if either: any child of a is equal to b or any child of a is an ancestor of b.


# Example 1:

# ￼
# Input: root = [8,3,10,1,6,null,14,null,null,4,7,13]
# Output: 7
# Explanation: We have various ancestor-node differences, some of which are given below :
# |8 - 3| = 5
# |3 - 7| = 4
# |8 - 1| = 7
# |10 - 13| = 3
# Among all possible differences, the maximum value of 7 is obtained by |8 - 1| = 7.
# Example 2:

# ￼
# Input: root = [1,null,2,null,0,3]
# Output: 3


# Constraints:

# The number of nodes in the tree is in the range [2, 5000].
# 0 <= Node.val <= 105


# ---------------------------------------Runtime 38 ms Beats 85.58% Memory 19.06 MB Beats 73.40%---------------------------------------

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        self.curr_diff: int = 0

        def dfs(node: Optional[TreeNode], min_val: int, max_val: int) -> None:
            """
            Intuition:
                declare a function `dfs` with three parameters `node`,
                'min_val', 'max_val'.
                node - is it the current node
                min_val - minimum value of previous ancestors
                max_val - maximum value of previous ancestors

                In every iteration calculate the current difference
                between previous difference, difference between
                the min value and current value of the node and
                difference between the max value and current value of the node.
            """
            if node:
                self.curr_diff = max(
                    self.curr_diff,
                    abs(min_val - node.val),
                    abs(max_val - node.val),
                )
                min_val = min(min_val, node.val)
                max_val = max(max_val, node.val)
                dfs(node.left, min_val, max_val)
                dfs(node.right, min_val, max_val)

        dfs(root, root.val, root.val)
        return self.curr_diff
