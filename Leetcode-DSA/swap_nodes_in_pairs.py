from __future__ import annotations
from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        return f"ListNode({self.val})"


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Swap every two adjacent nodes in the linked list and return the head.

        Uses a dummy node to simplify pointer manipulation and iterates
        through the list swapping nodes in pairs.
        """
        dummy = ListNode(0, head)
        prev = dummy

        while prev.next is not None and prev.next.next is not None:
            first = prev.next
            second = first.next

            # Swap the pair
            first.next = second.next
            second.next = first
            prev.next = second

            # Move prev forward by two nodes
            prev = first

        return dummy.next

    def swapPairsTwoPointer(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Swap every two adjacent nodes using a two-pointer style approach.

        This version walks through the list with curr and next_node, updating
        links in place for each adjacent pair.
        """
        if head is None or head.next is None:
            return head

        new_head = head.next
        prev = None
        curr = head

        while curr is not None and curr.next is not None:
            next_node = curr.next
            following = next_node.next

            # Swap current pair
            next_node.next = curr
            curr.next = following

            if prev is not None:
                prev.next = next_node

            prev = curr
            curr = following

        return new_head


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
        ([1, 2, 3, 4], [2, 1, 4, 3]),
        ([], []),
        ([1], [1]),
        ([1, 2, 3], [2, 1, 3]),
    ]

    for i, (values, expected) in enumerate(tests, start=1):
        head = build_list(values)
        swapped = sol.swapPairs(head)
        output = list_to_array(swapped)
        print(f"Test {i}: input={values}")
        print(f"Output: {output}")
        print(f"Expected: {expected}")
        print(f"Match: {output == expected}")
        print()