# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    result = 0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.height(root)
        return self.result
    def height(self,node: Optional[TreeNode], ) -> int:
        if not node:
            return 0
        
        L = self.height(node.left)
        R = self.height(node.right)
        self.result = max(self.result, L + R)      
        return 1 + max(L, R)         
    

        



         
 