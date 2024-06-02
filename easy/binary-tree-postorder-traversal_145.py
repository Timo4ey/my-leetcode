# Given the root of a binary tree, return the postorder traversal of its nodes' values.

# Example 1:

# ￼
# Input: root = [1,null,2,3]
# Output: [3,2,1]
# Example 2:

# Input: root = []
# Output: []
# Example 3:

# Input: root = [1]
# Output: [1]

# Constraints:

# The number of the nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100

# Follow up: Recursive solution is trivial, could you do it iteratively?


# ---------------------------------------Runtime 31 ms Beats 79.35% Memory 16.44 MB Beats 74.63%---------------------------------------

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.res = []

        def dfs(node: Optional[TreeNode]) -> None:
            if node:
                dfs(node=node.left)
                dfs(node=node.right)

                self.res.append(node.val)

        dfs(root)
        return self.res
