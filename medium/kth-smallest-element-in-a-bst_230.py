# Given the root of a binary search tree, and an integer k,
# return the kth smallest value (1-indexed)
# of all the values of the nodes in the tree.

# Example 1:

# ￼
# Input: root = [3,1,4,null,2], k = 1
# Output: 1
# Example 2:

# ￼
# Input: root = [5,3,6,2,4,null,null,1], k = 3
# Output: 3


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional

# ---------------------------------------Runtime 67 ms Beats 59.77% Memory 20.4 MB Beats 82.14%---------------------------------------


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        output = []

        def getNums(node):
            if not node:
                return
            getNums(node.left)
            if len(output) == k:
                return
            output.append(node.val)
            getNums(node.right)

        getNums(root)

        return output[-1]
