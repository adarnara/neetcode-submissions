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
# [0,1,2,3]
# [1,0, 2, 3]
# [1, 2, 0, 3]
# [1, 2, 3, 0]



        