# You are given the root of a binary tree.

# A ZigZag path for a binary tree is defined as follow:

# Choose any node in the binary tree and a direction (right or left).
# If the current direction is right, move to the right child of the current node; otherwise, move to the left child.
# Change the direction from right to left or from left to right.
# Repeat the second and third steps until you can't move in the tree.
# Zigzag length is defined as the number of nodes visited - 1. (A single node has a length of 0).

# Return the longest ZigZag path contained in that tree.


# Example 1:

# ￼
# Input: root = [1,null,1,1,1,null,null,1,1,null,1,null,null,null,1]
# Output: 3
# Explanation: Longest ZigZag path in blue nodes (right -> left -> right).
# Example 2:

# ￼
# Input: root = [1,1,1,null,1,null,null,1,1,null,1]
# Output: 4
# Explanation: Longest ZigZag path in blue nodes (left -> right -> left -> right).
# Example 3:

# Input: root = [1]
# Output: 0
# ---------------------------------------Runtime 404 ms Beats 29.6% Memory 64.3 MB Beats 24.32%---------------------------------------


from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        def walk(tree: TreeNode, position, acc: int):
            if tree:
                self.res = max(self.res, acc)
                match position:
                    case "left":
                        walk(tree.left, "right", acc + 1)
                        walk(tree.right, "left", 1)
                    case "right":
                        walk(tree.left, "right", 1)
                        walk(tree.right, "left", acc + 1)

        walk(root, "left", 0)
        walk(root, "right", 0)
        return self.res
