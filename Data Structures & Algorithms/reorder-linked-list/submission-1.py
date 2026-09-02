
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
        temp = head
        tempCount = 0
        while temp!=None:
            temp=temp.next
            tempCount = tempCount+1
        mid = (tempCount + 1) // 2

        start = head
        i=0

        while i < mid:
            prev = start 
            start = start.next
            i +=1
            if i == mid:
                prev.next = None
        


        new = start
        newFinal = start
        new2 = new.next
        while new2 != None:
            tempnext = new2.next
            new2.next = new
            new = new2
            new2 = tempnext
        
        newFinal.next = None
        


        left = head
        right = new
        tempR = None
        tempL = None
        while right:
            if left:
                tempL = left.next
                left.next = right
            if right:
                tempR = right.next
                right.next = tempL
            right = tempR
            left = tempL
                
        return None