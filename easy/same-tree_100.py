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
