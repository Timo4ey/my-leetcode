# You are given the root of a binary search tree (BST) and an integer val.

# Find the node in the BST that the node's value equals val and return the subtree rooted with that node. If such a node does not exist, return null.


# Example 1:

# ￼
# Input: root = [4,2,7,1,3], val = 2
# Output: [2,1,3]
# Example 2:

# ￼
# Input: root = [4,2,7,1,3], val = 5
# Output: []
# ---------------------------------------Runtime 71 ms Beats 75.26% Memory 18.5 MB Beats 69.42%---------------------------------------


from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def searchBST(
        self, root: Optional[TreeNode], val: int
    ) -> Optional[TreeNode]:
        def iter(node):
            if node:
                return (
                    node
                    if node.val == val
                    else iter(node.left) or iter(node.right)
                )

        return iter(root)
