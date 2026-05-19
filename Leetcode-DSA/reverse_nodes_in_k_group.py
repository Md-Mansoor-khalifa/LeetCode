from __future__ import annotations
from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        return f"ListNode({self.val})"


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        Reverse nodes of the list k at a time and return the modified list.

        This solution uses O(1) extra memory by reversing groups in place.
        If the remaining nodes are fewer than k, they are left as is.
        """
        dummy = ListNode(0, head)
        group_prev = dummy

        while True:
            # Find the kth node from group_prev
            kth = self._get_kth_node(group_prev, k)
            if kth is None:
                break

            group_next = kth.next
            # Reverse the group
            prev = group_next
            curr = group_prev.next

            while curr is not group_next:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            # Reconnect the reversed group with the previous part
            tail = group_prev.next
            group_prev.next = kth
            group_prev = tail

        return dummy.next

    def _get_kth_node(self, start: ListNode, k: int) -> Optional[ListNode]:
        """Return the k-th node from start, or None if fewer than k nodes remain."""
        curr = start
        for _ in range(k):
            if curr is None:
                return None
            curr = curr.next
        return curr


def build_list(values: list[int]) -> Optional[ListNode]:
    dummy = ListNode(0)
    tail = dummy
    for value in values:
        tail.next = ListNode(value)
        tail = tail.next
    return dummy.next


def list_to_array(head: Optional[ListNode]) -> list[int]:
    result: list[int] = []
    node = head
    while node is not None:
        result.append(node.val)
        node = node.next
    return result


if __name__ == "__main__":
    sol = Solution()
    tests = [
        ([1, 2, 3, 4, 5, 6], 3, [3, 2, 1, 6, 5, 4])
    ]

    for i, (values, k, expected) in enumerate(tests, start=1):
        head = build_list(values)
        result = sol.reverseKGroup(head, k)
        output = list_to_array(result)
        print(f"Test {i}: values={values}, k={k}")
        print(f"Output: {output}")
        print(f"Expected: {expected}")
        print(f"Match: {output == expected}")
        print()