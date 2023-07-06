# Given the root of a binary tree, return its maximum depth.

# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

# Example 1:

# ￼
# Input: root = [3,9,20,null,null,15,7]
# Output: 3
# Example 2:

# Input: root = [1,null,2]
# Output: 2


from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# ---------------------------------------Runtime 52 ms Beats 83.74% Memory 19 MB Beats 12.97%---------------------------------------


# Time complexity O(n)
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def inner(node, depth=0):
            if not node:
                return depth
            return max(
                inner(node.left, depth=depth + 1),
                inner(node.right, depth=depth + 1),
            )

        return inner(root)


# Solution neetcode
# Type Stack
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        res = 0
        stack = [[root, res]]

        while stack:
            node, depth = stack.pop()

            if node:
                res = max(res, depth)
                stack.append([node.left, depth + 1])
                stack.append([node.right, depth + 1])
        return res
