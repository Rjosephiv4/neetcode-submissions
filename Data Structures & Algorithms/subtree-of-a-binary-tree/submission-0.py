# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def equal(node1, node2):
            if not node1 and not node2:
                return True
            
            if not node1 or not node2:
                return False

            if node1.val == node2.val and equal(node1.left,node2.left) and equal(node1.right,node2.right):
                return True

        def test(root2, sub2):
            if root2 == None:
                return False
            if equal(root2,sub2):
                return True
            elif test(root2.right,sub2) or test(root2.left, sub2):
                return True
            
            return False
        return test(root, subRoot)
