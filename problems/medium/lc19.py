class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        dummy = ListNode(0, head)
        left = dummy
        right = head
        for _ in range(n):
            right = right.next

        while right is not None:
            left = left.next
            right = right.next

        left.next = left.next.next

        return dummy.next
