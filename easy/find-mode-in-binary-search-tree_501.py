# Given the root of a binary search tree (BST) with duplicates,
# return all the mode(s) (i.e., the most frequently occurred element) in it.

# If the tree has more than one mode, return them in any order.

# Assume a BST is defined as follows:

# The left subtree of a node contains only nodes with keys less than or equal to the node's key.
# The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
# Both the left and right subtrees must also be binary search trees.

# Example 1:

# Input: root = [1,null,2,2]
# Output: [2]
# Example 2:

# Input: root = [0]
# Output: [0]

# ---------------------------------------Runtime 1565 ms Beats 5.4% Memory 20.7 MB Beats 56.6%---------------------------------------


from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        hash_map = dict()

        def bst(node):
            if node:
                val = node.val
                hash_map[val] = hash_map.get(val, 0) + 1
                bst(node.left)
                bst(node.right)

        bst(root)
        return [k for k, v in hash_map.items() if v == max(hash_map.values())]
