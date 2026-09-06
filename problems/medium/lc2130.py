from problems.medium.lc19 import ListNode


class Solution:
    def find_middle(self, head: ListNode | None) -> ListNode | None:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def reverseList(self, head: ListNode | None) -> ListNode | None:
        prev = None
        curr = head
        while curr:
            tmp = curr
            curr = curr.next
            tmp.next = prev
            prev = tmp
        return prev

    def pairSum(self, head: ListNode | None) -> int:
        mid_node = self.find_middle(head)
        reversed_mid = self.reverseList(mid_node)
        left, right = head, reversed_mid
        max_sum = 0
        while right:
            max_sum = max(max_sum, (left.val + right.val))
            left = left.next
            right = right.next
        return max_sum
