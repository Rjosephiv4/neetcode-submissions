# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        height = self.height(root)
        if height == -1:
            return False
        else:
            return True
    def height(self, root):
        if not root:
            return 0
        left = 0
        right = 0

        if root.left:
            left = self.height(root.left)
        if root.right:
            right = self.height(root.right)

        if abs(left - right) > 1:
            return -1
        
        if left == -1 or right == -1:
            return -1
        else:
            return max(left,right) + 1