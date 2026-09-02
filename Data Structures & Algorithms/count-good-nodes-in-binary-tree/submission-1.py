# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        def helper(node, maxVal):
            nonlocal count
            if not node:
                return 

            if maxVal <= node.val:
                maxVal = node.val
                count = count+1
            
            helper(node.left,maxVal)
            helper(node.right,maxVal)
        

        helper(root,float("-inf"))
        return count
            



