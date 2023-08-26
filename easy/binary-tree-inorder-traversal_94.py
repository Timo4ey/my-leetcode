# Given the root of a binary tree, return the inorder traversal of its nodes' values.


# Example 1:

# ￼
# Input: root = [1,null,2,3]
# Output: [1,3,2]
# Example 2:

# Input: root = []
# Output: []
# Example 3:

# Input: root = [1]
# Output: [1]
# ---------------------------------------Runtime 41 ms Beats 62.86% Memory 16.3 MB Beats 72.25%---------------------------------------


from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        store = []

        def dfs(node):
            if node:
                dfs(node.left)
                store.append(node.val)
                dfs(node.right)

        dfs(root)

        return store
