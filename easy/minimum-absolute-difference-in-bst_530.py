# Given the root of a Binary Search Tree (BST),
# return the minimum absolute difference between
# the values of any two different nodes in the tree.

# Example 1:

# ￼
# Input: root = [4,2,6,1,3]
# Output: 1
# Example 2:

# ￼
# Input: root = [1,0,48,null,null,12,49]
# Output: 1

# # ---------------------------------------Runtime 64 ms Beats 14.59% Memory 18.6 MB Beats 67.25%---------------------------------------


from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        values: list[int] = []

        def bst(node: TreeNode):
            if node:
                nonlocal values
                values.append(node.val)
                bst(node.left)
                bst(node.right)

        bst(root)
        values.sort()

        res = float("INF")
        for i in range(len(values) - 1):
            res = min(
                res,
                abs(values[i] - values[i - 1]),
                abs(values[i + 1] - values[i]),
            )

        return res
