from __future__ import annotations
from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        return f"ListNode({self.val})"


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        Remove the nth node from the end of the linked list and return the head.

        Uses a dummy node and two-pointer (fast/slow) technique so that the
        node to remove can be found in one pass.
        """
        dummy = ListNode(0, head)
        fast = dummy
        slow = dummy

        # Move fast n+1 steps ahead so slow lands on the node before target
        for _ in range(n + 1):
            fast = fast.next

        while fast is not None:
            fast = fast.next
            slow = slow.next

        # Remove nth node from end
        if slow.next is not None:
            slow.next = slow.next.next

        return dummy.next


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
    while node:
        result.append(node.val)
        node = node.next
    return result


if __name__ == "__main__":
    sol = Solution()

    tests = [
        ([1, 2, 3, 4, 5], 2, [1, 2, 3, 5]),
        ([1], 1, []),
        ([1, 2], 1, [1]),
    ]

    for i, (values, n, expected) in enumerate(tests, start=1):
        head = build_list(values)
        result = sol.removeNthFromEnd(head, n)
        out = list_to_array(result)
        print(f"Test {i}: input={values}, n={n}")
        print(f"Output: {out}")
        print(f"Expected: {expected}")
        print()
