# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.maxDepthHelper(root, 0)
    
    def maxDepthHelper(self, root:Optional[TreeNode], maxD) -> int:
        left = 0
        right = 0
        if not root:
            return maxD
        if root.left:
            left =  1 + self.maxDepthHelper(root.left, maxD)
        if root.right:
            right = 1 + self.maxDepthHelper(root.right, maxD)
        
        return max(maxD + 1, max(left, right))