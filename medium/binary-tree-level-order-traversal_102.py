# Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).


# Example 1:

# ￼
# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[9,20],[15,7]]
# Example 2:

# Input: root = [1]
# Output: [[1]]
# Example 3:

# Input: root = []
# Output: []

# ---------------------------------------Runtime 41 ms Beats 79.61% Memory 14.2 MB Beats 100%---------------------------------------


# My Solution

from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return root
        gather = []
        gather.append([root.val])
        q = deque()
        q.extend([root.left, root.right])
        while q:
            store = []
            temp = [[]]
            counter = 0
            for node in q:
                if isinstance(node, TreeNode):
                    temp[0].append(node.val)
                    store.extend([node.left, node.right])
                counter += 1

            if temp[0]:
                gather.extend(temp)
            temp.clear()
            if store:
                q.extend(store)
            for x in range(counter):
                q.popleft()

        return gather
