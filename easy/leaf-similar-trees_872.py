from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Consider all the leaves of a binary tree, from left to right order, the values of those leaves form a leaf value sequence.

# ￼

# For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).

# Two binary trees are considered leaf-similar if their leaf value sequence is the same.

# Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.


# Example 1:

# ￼
# Input: root1 = [3,5,1,6,2,9,8,null,null,7,4], root2 = [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]
# Output: true
# Example 2:

# ￼
# Input: root1 = [1,2,3], root2 = [1,3,2]
# Output: false


# ---------------------------------------Runtime 36 ms Beats 89.2% Memory 16.5 MB Beats 25.10%---------------------------------------


class Solution:
    def leafSimilar(
        self, root1: Optional[TreeNode], root2: Optional[TreeNode]
    ) -> bool:
        def iter(node: TreeNode, acc: list):
            if not node:
                return
            if not node.left and not node.right:
                acc.append(node.val)
                return
            iter(node.left, acc), iter(node.right, acc)

        acc1 = []
        acc2 = []
        iter(root1, acc1), iter(root2, acc2)
        return acc1 == acc2
