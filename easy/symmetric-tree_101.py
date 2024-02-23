# Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

# Example 1:

# ￼
# Input: root = [1,2,2,3,4,4,3]
# Output: true
# Example 2:

# ￼
# Input: root = [1,2,2,null,3,null,3]
# Output: false


# Constraints:

# The number of nodes in the tree is in the range [1, 1000].
# -100 <= Node.val <= 100


# Follow up: Could you solve it both recursively and iteratively?

# ---------------------------------------Runtime 41 ms Beats 34.45% Memory 16.67 MB Beats 51.99%---------------------------------------

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        self.left = "left"
        self.right = "right"
        self.right_store = []
        self.left_store = []

        def dfs(node: Optional[TreeNode], store: List[int], flag: str) -> None:
            hasattr(node, "val") and store.append(node.val) or store.append(
                None
            )
            if node:
                flag_2 = self.left if flag == self.right else self.right
                dfs(getattr(node, flag), store, flag)
                dfs(getattr(node, flag_2), store, flag)

        dfs(root.left, self.left_store, self.left)
        dfs(root.right, self.right_store, self.right)
        return self.right_store == self.left_store
