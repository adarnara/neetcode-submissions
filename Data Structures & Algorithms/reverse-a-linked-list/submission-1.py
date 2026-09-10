# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        prev = None
        curr = head
        
        while curr:
            nxt = curr.next  # Save next node
            curr.next = prev # Reverse pointer
            prev = curr      # Advance prev
            curr = nxt       # Advance curr
            
        return prev  # prev is now the new head


# [0,1,2,3] -> curr = 0, prev = none

#itr 1
#=====
# nxt = 1, curr.next = None, prev = 0, curr = 1

#itr 2
#=====
# nxt = 2, curr.next = 0, prev = 1, curr = 2

#itr 3
#=====
# nxt = 3, curr.next = 1, prev = 2, curr = 3

#itr 4
#=====
# nxt = null, curr.next = 2, prev = 3, curr = null


''' Recursive solution
if not head or not head.next:
            return head

        # Recursively reverse the sublist starting at head.next
        new_head = self.reverseList(head.next)

        # Make the next node point back to current node
        head.next.next = head
        head.next = None

        return new_head
'''




        