class Optional(list):
    pass




class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        r = l = 0
        
        def walk(tree, position):
            if tree.left and tree.right:
                count += 1
            while tree:
                if tree and position == "right":
                    if tree.left:
                        count += 1
                        tree =  tree.left
                        position = "left"
                    elif tree.right and not tree.left:
                        tree = tree.right
                        position = "right"
                    else:
                        break
                elif tree and position == "left":
                    if tree.right:
                        count += 1
                        tree =  tree.right
                        position = "right"
                    elif tree.left and not tree.right:
                        tree = tree.left
                        position = "left"
                    else:
                        break
                    
            return count
        r = walk(root.right, 'right')
        l = walk(root.left, 'left')
        print(l,r)
        return max(r, l)


tree = TreeNode(1, left=TreeNode(1), right=TreeNode(1))
tree.right = TreeNode(1)
tree.left = TreeNode(1, right=TreeNode(1))
tree.left.right = TreeNode(1, left=TreeNode(1), right=TreeNode(2))
tree.left.right.left = TreeNode(1, right=TreeNode(1))



sol = Solution()

sol.longestZigZag(tree)













# class Solution:
#     def longestZigZag(self, root: Optional[TreeNode]) -> int:
#         count = r = l = 0
#         count = 1
#         def walk(tree, position):
#             nonlocal count
#             if position == 'left' and tree.right:
#                 count += 1
#                 return walk(tree.right, 'right')
#             if position == 'right' and tree.left:
#                 count += 1
#                 return walk(tree.left, 'left')
#             return count
#         if root.left and root.right:
#             r = walk(root.right, 'right')
#             l =  walk(root.left, 'left')
#         elif root.left:
#             l =  walk(root.left, 'left')
#         elif root.right:
#             r = walk(root.right, 'right')
#         return max(r, l)