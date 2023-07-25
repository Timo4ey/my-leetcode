# Given an array of integers preorder, which represents the preorder traversal of a BST (i.e., binary search tree), construct the tree and return its root.

# It is guaranteed that there is always possible to find a binary search tree with the given requirements for the given test cases.

# A binary search tree is a binary tree where for every node, any descendant of Node.left has a value strictly less than Node.val, and any descendant of Node.right has a value strictly greater than Node.val.

# A preorder traversal of a binary tree displays the value of the node first, then traverses Node.left, then traverses Node.right.


# Example 1:

# ￼
# Input: preorder = [8,5,1,7,10,12]
# Output: [8,5,10,1,7,null,12]
# Example 2:

# Input: preorder = [1,3]
# Output: [1,null,3]
# ---------------------------------------Runtime 54 ms Beats 49.84% Memory 16.3 MB Beats 71.50%---------------------------------------


from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def bstFromPreorder(self, preorder: list[int]) -> Optional[TreeNode]:
        stack = deque(preorder)
        tree = TreeNode(stack.popleft())

        def insert(node):
            if stack[0] > node.val:
                if not node.right:
                    node.right = TreeNode(stack.popleft())
                    return
                else:
                    insert(node.right)

            elif stack[0] < node.val:
                if not node.left:
                    node.left = TreeNode(stack.popleft())
                    return
                else:
                    insert(node.left)

        while stack:
            insert(tree)

        return tree
