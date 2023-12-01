# Given a binary tree, find its minimum depth.

# The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

# Note: A leaf is a node with no children.

# Example 1:

# ￼
# Input: root = [3,9,20,null,null,15,7]
# Output: 2
# Example 2:

# Input: root = [2,null,3,null,4,null,5,null,6]
# Output: 5


# ---------------------------------------Runtime 407 ms Beats 66.51% Memory 58.2 MB Beats 40.61%---------------------------------------

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        res = False

        def dfs(node: TreeNode | None, depth: int):
            nonlocal res
            if (
                node
                and node.left is not None
                or node
                and node.right is not None
            ):
                dfs(node.left, depth + 1)
                dfs(node.right, depth + 1)

            elif node and node.left is None and node.right is None:
                if res is False:
                    res = depth
                res = min(res, depth)

        dfs(root, 1)

        return int(res)
