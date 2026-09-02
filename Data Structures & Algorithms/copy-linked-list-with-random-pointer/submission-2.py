"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        refrences = {}

        temp = head

        while temp:
            newNode = Node(temp.val, None, None)

            refrences[temp] = newNode
            temp = temp.next
        

        temp = head
        while temp:
            if temp.next != None:
                refrences[temp].next = refrences[temp.next]
            if temp.random != None:
                refrences[temp].random = refrences[temp.random]
            temp=temp.next
        
        return refrences[head]
            
        