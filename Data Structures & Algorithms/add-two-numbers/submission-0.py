# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        carry = 0
        dummy = ListNode(0,None)
        curr = dummy
        ln1 = l1
        ln2 = l2
        while ln1 or ln2:
            result = 0
            if ln1 and ln2: 
                result = ln1.val + ln2.val + carry
            elif ln2:
                result = ln2.val + carry
            else:
                result = ln1.val + carry
            vals = result % 10
            carry = result // 10

            curr.next = ListNode(vals, None)

            if ln1:
                ln1 = ln1.next
            if ln2:
                ln2 = ln2.next
            curr = curr.next
        
        if carry != 0:
            curr.next = ListNode(carry, None)
        return dummy.next


