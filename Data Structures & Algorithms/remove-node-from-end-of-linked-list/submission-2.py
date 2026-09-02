# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        num = 0

        temp = head
        while temp:
            num +=1
            temp = temp.next

        node = num - n 

        dummy = ListNode(0, head)


        prev = dummy
        temp = head
        i = 0
        while i < node:
            i +=1
            prev = temp
            temp = temp.next
        prev.next = temp.next


        return dummy.next

        
