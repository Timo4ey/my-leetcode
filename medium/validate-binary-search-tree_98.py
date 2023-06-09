# Definition for a binary tree node.
class Optional(list):
    ...


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # stock behaves like stack (last in first out)
        stack = []
        # prev it's the previous node
        prev = None

        # while root and stock are not empty
        while root or stack:
            # while root is not empty
            while root:
                # add in stock nodes until root is not run out
                stack.append(root)
                # goint left until left is not None
                root = root.left
            # getting the last element
            root = stack.pop()
            # prev bigger or equal current val so return false
            if prev and root.val <= prev.val:
                return False
            # prev takes current root
            prev = root
            # the root switches branch to right
            root = root.right
        # if root and stock run out it's mean it's ok BST
        return True


# проходим запоминаем ноды в список на припример
# сравнивает для макс мин больше или меньше

tree = TreeNode(1)
tree.left = TreeNode(4)
tree.right = TreeNode(5)
tree.left.right = TreeNode(3)
tree.right.right = TreeNode(4)
tree.right.left = TreeNode(2)


if __name__ == "__main__":
    s = Solution()
    r = s.isValidBST(tree)
    print(r)


# [0]
# [1,4,5,null,3,2,4]
# [6,4,8,3,5,7,9]
# [0,-1]
# [0,null,2,1,3, null, null, 2,4]

# [0,-1]
# [0,null, 1]
# [0]
