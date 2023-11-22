# Given the root of a binary tree, invert the tree, and return its root.

# Example 1:

# ￼
# Input: root = [4,2,7,1,3,6,9]
# Output: [4,7,2,9,6,3,1]
# Example 2:

# ￼
# Input: root = [2,1,3]
# Output: [2,3,1]
# Example 3:

# Input: root = []
# Output: []


# ---------------------------------------Runtime 43 ms Beats 82.11% Memory 16.4 MB Beats 34.13%---------------------------------------

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Time complexity O(n)
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #       root
        #   right <-> left
        # r <-> l   r <-> l
        if root is None:
            return

        head = root
        left = head.left
        right = head.right
        head.left, head.right = right, left
        if left:
            self.invertTree(left)
        if right:
            self.invertTree(right)

        return head


# Solution @jyot_150
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        return (
            TreeNode(
                root.val,
                self.invertTree(root.right),
                self.invertTree(root.left),
            )
            if root
            else None
        )
