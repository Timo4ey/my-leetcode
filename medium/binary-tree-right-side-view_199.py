# Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.


# Example 1:

# ￼
# Input: root = [1,2,3,null,5,null,4]
# Output: [1,3,4]
# Example 2:

# Input: root = [1,null,3]
# Output: [1,3]
# Example 3:

# Input: root = []
# Output: []

# ---------------------------------------Runtime 37 ms Beats 85.56% Memory 16.5 MB Beats 7.15%---------------------------------------


from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> list[int]:
        self.indexes = set()
        self.res = []

        def iter(node: TreeNode, depth: int) -> None:
            if node:
                if depth not in self.indexes:
                    self.indexes.add(depth)
                    self.res.append(node.val)
                iter(node.right, depth + 1)
                iter(node.left, depth + 1)

        iter(root, 0)

        return self.res
