# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Using fast and slow pointers.
        if not head or not head.next or not head.next.next:
            return None
        
        slow, fast = head.next, head.next.next
        
        while slow != fast:
            if not fast or not fast.next:
                return None
            slow, fast = slow.next, fast.next.next
        
        slow = head
        while slow != fast:
            slow, fast = slow.next, fast.next
        return slow
