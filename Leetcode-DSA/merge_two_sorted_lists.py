from __future__ import annotations
from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        return f"ListNode({self.val})"


class Solution:
    def mergeTwoLists(
        self,
        list1: Optional[ListNode],
        list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        """
        Merge two sorted linked lists into one sorted list.

        Uses a dummy node and iterates through both lists simultaneously,
        appending the smaller current node from each list.
        """
        dummy = ListNode(0)
        tail = dummy

        while list1 is not None and list2 is not None:
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        tail.next = list1 if list1 is not None else list2
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
    while node is not None:
        result.append(node.val)
        node = node.next
    return result


if __name__ == "__main__":
    sol = Solution()
    tests = [
        ([1, 2, 4], [1, 3, 4], [1, 1, 2, 3, 4, 4]),
        ([], [], []),
        ([], [0], [0]),
    ]

    for i, (list1_vals, list2_vals, expected) in enumerate(tests, start=1):
        list1 = build_list(list1_vals)
        list2 = build_list(list2_vals)
        merged = sol.mergeTwoLists(list1, list2)
        output = list_to_array(merged)
        print(f"Test {i}: list1={list1_vals}, list2={list2_vals}")
        print(f"Output: {output}")
        print(f"Expected: {expected}")
        print()