# A binary tree is uni-valued if every node in the tree has the same value.

# Given the root of a binary tree, return true if the given tree is uni-valued, or false otherwise.


# Example 1:

# ￼
# Input: root = [1,1,1,1,1,null,1]
# Output: true
# Example 2:

# ￼
# Input: root = [2,2,2,5,2]
# Output: false
# ---------------------------------------Runtime 44 ms Beats 21.63% Memory 16.3 MB Beats 28.81%---------------------------------------


from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        arr = set()

        def iter(node):
            nonlocal arr
            if node:
                arr.add(node.val)
                if len(arr) > 1:
                    return
                iter(node.left)
                iter(node.right)

        iter(root)
        return len(arr) == 1
