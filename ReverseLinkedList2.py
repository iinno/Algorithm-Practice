# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # No need to do anything if only one node needs to be revsersed.
        if left == right:
            return head
        
        link_one, link_two = None, None
        link_start = head
        temp_node = head
        
        # Find the node where the link break starts (link_one), first node to reverse (link_start) and where the link break ends (link_two).
        for i in range(right):
            # Found where the link break starts.
            if i == left-2:
                link_one = temp_node
                link_start = temp_node.next
            temp_node = temp_node.next
        link_two =  temp_node
        
        # Reverse the significant segment of linked list
        for i in range(right-left+1):
            temp = link_start.next
            link_start.next = link_two
            link_two = link_start
            link_start = temp
            # link_start, link_two, link_start.next = link_start.next, link_start, link_two
           
        # If link_one than there is/are node/nodes before the significant segment to be reversed begins. Else, the first node is part of the segment to be reversed.
        if link_one:
            link_one.next = link_two
            return head
        else:
            return link_two
