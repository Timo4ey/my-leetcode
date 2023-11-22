# Given the roots of two binary trees p and q, write a function to check if they are the same or not.

# Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

# Example 1:

# ￼
# Input: p = [1,2,3], q = [1,2,3]
# Output: true
# Example 2:

# ￼
# Input: p = [1,2], q = [1,null,2]
# Output: false
# Example 3:

# ￼
# Input: p = [1,2,1], q = [1,1,2]
# Output: false

# ---------------------------------------Runtime 42 ms Beats 28.2% Memory 16.3 MB Beats 60.18%---------------------------------------


from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Time complexity O(n2)
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        left = []
        right = []
        if p and not q or q and not p:
            return False
        if not p and not q:
            return True
        if p.val != q.val:
            return False
        left.append(self.isSameTree(p.left, q.left))
        right.append(self.isSameTree(p.right, q.right))
        return all(left) == True and all(right) == True
