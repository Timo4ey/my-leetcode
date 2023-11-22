# Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

# A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.


# Example 1:

# ￼
# Input: root = [3,4,5,1,2], subRoot = [4,1,2]
# Output: true
# Example 2:

# ￼
# Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
# Output: false


# ---------------------------------------Runtime 113 ms Beats 92.27% Memory 17.6 MB Beats 57.60%---------------------------------------
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Time complexity O(n*m)
class Solution:
    def isSubtree(
        self, root: Optional[TreeNode], subRoot: Optional[TreeNode]
    ) -> bool:
        def dfs(node):
            if not node:
                return False
            return (
                True
                if is_identical(node, subRoot)
                else dfs(node.left) or dfs(node.right)
            )

        def is_identical(node1, node2):
            if not node1 or not node2:
                return not node1 and not node2

            return (
                node1.val == node2.val
                and is_identical(node1.left, node2.left)
                and is_identical(node1.right, node2.right)
            )

        return dfs(root)
