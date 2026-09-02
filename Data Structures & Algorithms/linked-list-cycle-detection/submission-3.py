# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False
        
        slow = head 
        fast = head.next
        while fast != None:
            if slow.val == fast.val:
                return True
            
            i = 0
            while fast != None and i < 2:
                i+=1
                fast = fast.next
            slow = slow.next

        return False