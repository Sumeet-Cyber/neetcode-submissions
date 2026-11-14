# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        node = ListNode()
        node.next = head
        prev = node
        while head:
            if head.val == val:
                prev.next = head.next
            else:
                # prev = prev.next
                prev = head
            head = head.next
        return node.next