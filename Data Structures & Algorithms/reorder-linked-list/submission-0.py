# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        two = slow.next
        slow.next = None

        prev = None
        curr = two
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        one, two = head, prev
        while two:
            t1, t2 = one.next, two.next
            one.next = two
            two.next = t1
            one = t1
            two = t2
            