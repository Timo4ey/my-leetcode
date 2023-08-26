# Given the root of a binary tree, return the preorder traversal of its nodes' values.


# Example 1:

# ￼
# Input: root = [1,null,2,3]
# Output: [1,2,3]
# Example 2:

# Input: root = []
# Output: []
# Example 3:

# Input: root = [1]
# Output: [1]


# Definition for a binary tree node.
# ---------------------------------------Runtime 41 ms Beats 63.60% Memory 16.2 MB Beats 72.15%---------------------------------------


from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        store = []

        def dfs(node):
            if node:
                store.append(node.val)
                dfs(node.left)
                dfs(node.right)

        dfs(root)

        return store
