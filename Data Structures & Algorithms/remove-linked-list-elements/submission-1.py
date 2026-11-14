# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        node = ListNode()
        node.next = head
        prev, curr = node, head
        while curr:
            if curr.val == val:
                prev.next = curr.next
            else:
                # prev = prev.next
                prev = curr
            curr = curr.next
        return node.next