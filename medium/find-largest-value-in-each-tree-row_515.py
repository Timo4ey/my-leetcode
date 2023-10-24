# Given the root of a binary tree, return an array
# of the largest value in each row of the tree (0-indexed).

# Example 1:

# ￼
# Input: root = [1,3,2,5,3,null,9]
# Output: [1,3,9]
# Example 2:

# Input: root = [1,2,3]
# Output: [1,3]

# ---------------------------------------Runtime 49 ms Beats 65.94% Memory 19.3 MB Beats 14.3%---------------------------------------


from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        items = []

        def iter(node, depth=0):
            if node:
                if len(items) == depth:
                    items.append(node.val)
                else:
                    items[depth] = max(items[depth], node.val)

                depth += 1
                iter(node.left, depth)
                iter(node.right, depth)

        iter(root)
        return items
