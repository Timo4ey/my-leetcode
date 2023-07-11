# Given the root of a binary tree, return the length of the diameter of the tree.

# The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

# The length of a path between two nodes is represented by the number of edges between them.


# Example 1:

# ￼
# Input: root = [1,2,3,4,5]
# Output: 3
# Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].
# Example 2:

# Input: root = [1,2]
# Output: 1
# ---------------------------------------Runtime 50 ms Beats 95.21% Memory 18.7 MB Beats 46.64%---------------------------------------

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = [0]

        def inner(root):
            if not root:
                return -1
            left = inner(root.left)
            right = inner(root.right)
            res[0] = max(res[0], (2 + left + right))
            return 1 + max(left, right)

        inner(root)
        return res[0]


# Solution @zayne-siew
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Implement depth
        def depth(node: Optional[TreeNode]) -> int:
            return 1 + max(depth(node.left), depth(node.right)) if node else 0

        return depth(root.left) + depth(root.right)  # calculate diameter
