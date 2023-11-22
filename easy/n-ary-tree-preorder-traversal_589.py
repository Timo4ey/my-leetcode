# Given the root of an n-ary tree, return the preorder traversal of its nodes' values.

# Nary-Tree input serialization is represented in their level order traversal. Each group of children is separated by the null value (See examples)

# Example 1:

# Input: root = [1,null,3,2,4,null,5,6]
# Output: [1,3,5,6,2,4]
# Example 2:

# ￼

# Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
# Output: [1,2,3,6,7,11,14,4,8,12,5,9,13,10]

# ---------------------------------------Runtime 57 ms Beats 31.20% Memory 16.5 MB Beats 100%---------------------------------------

from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


# My solution


class Solution:
    def preorder(self, root: Node) -> List[int]:
        counter = []
        if not root:
            return root
        value = root.val
        children = root.children
        if not children:
            return [value]
        counter.append(value)

        counter.extend(map(lambda x: self.preorder(x), children))
        output = []
        for i in counter:
            if isinstance(i, list):
                output.extend(i)
            else:
                output.append(i)
        return output


# Solution shivam_1110
# Complexity
# Time complexity: O(N)
# Space complexity: O(N)


class Solution:
    def preorder(self, root: "Node") -> List[int]:
        ans = []

        def helper(curr=root):
            nonlocal ans
            if curr:
                ans.append(curr.val)
                for i in curr.children:
                    helper(i)

        helper()
        return ans
