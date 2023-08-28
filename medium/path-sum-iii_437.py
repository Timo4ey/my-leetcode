# Given the root of a binary tree and an integer targetSum, return the number of paths where the sum of the values along the path equals targetSum.

# The path does not need to start or end at the root or a leaf, but it must go downwards (i.e., traveling only from parent nodes to child nodes).


# Example 1:

# ￼
# Input: root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
# Output: 3
# Explanation: The paths that sum to 8 are shown.
# Example 2:

# Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
# Output: 3

# ---------------------------------------Runtime 603 ms Beats 32.85% Memory 17.8 MB Beats 67.97%---------------------------------------


from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.res = 0

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def iter(node: TreeNode, state: bool, acc: int):
            if node:
                # substract current head
                acc -= node.val
                if acc == 0:
                    # if `acc` equal 0 it means that we find the  number
                    # of paths where the sum of the values along the path equals targetSum
                    self.res += 1

                # check from current head
                iter(node.left, False, acc)
                iter(node.right, False, acc)

                if state:
                    # set children of current head to heads to find any options
                    iter(node.left, True, targetSum),
                    iter(node.right, True, targetSum),

        iter(root, True, targetSum)
        return self.res
