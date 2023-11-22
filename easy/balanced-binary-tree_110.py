# Given a binary tree, determine if it is
# height-balanced
# .


# Example 1:

# ￼
# Input: root = [3,9,20,null,null,15,7]
# Output: true
# Example 2:

# ￼
# Input: root = [1,2,2,3,3,null,null,4,4]
# Output: false
# Example 3:

# Input: root = []
# Output: true


# ---------------------------------------Runtime 62 ms Beats 80.6% Memory 21 MB MB Beats 79.29%---------------------------------------

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Solution Time complexity O(n)
class Solution:
    def countDepth(self, root):
        if not root:
            return 0

        left = self.countDepth(root.left)
        right = self.countDepth(root.right)
        if left < 0 or right < 0 or abs(left - right) > 1:
            return -1
        return max(left, right) + 1

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.countDepth(root) >= 0


# Solution @neetcode


class Solution:
    def countDepth(self, root):
        if not root:
            return [True, 0]

        left = self.countDepth(root.left)
        right = self.countDepth(root.right)
        is_balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1
        return [is_balanced, max([left[1], right[1]]) + 1]

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.countDepth(root)[0]
