# Given the root of a binary tree, return the sum of values of its deepest leaves.

# Example 1:

# Input: root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
# Output: 15
# Example 2:

# Input: root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
# Output: 19


from functools import reduce
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Solution
# Time Complexity O(n)
# ---------------------------------------Runtime 265 ms Beats 9.91% Memory 19.8 MB Beats 98.64%---------------------------------------


class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        nodes = []
        maxDepth = 0
        if root and not root.left and not root.right:
            return root.val

        def dfs(node: TreeNode, depth: int):
            if node and not node.left and not node.right:
                nonlocal maxDepth
                maxDepth = max(maxDepth, depth)
                nodes.append([node.val, depth])
                return [node.val, depth]
            if not node:
                return 0

            return [
                dfs(node.left, depth=depth + 1),
                dfs(node.right, depth=depth + 1),
            ]

        dfs(root.left, 0)
        dfs(root.right, 0)
        nodes = list(filter(lambda x: x[1] == maxDepth, nodes))
        return reduce(lambda acc, x: acc + x[0], nodes, 0)
