from problems.medium.lc19 import ListNode


class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        prev = None
        curr = head
        while curr:
            tmp = curr
            curr = curr.next
            tmp.next = prev
            prev = tmp
        return prev
