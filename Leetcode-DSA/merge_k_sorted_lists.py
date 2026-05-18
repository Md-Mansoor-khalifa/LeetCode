
from typing import List, Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        return f"ListNode({self.val})"


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        Merge k sorted linked lists into one sorted list.

        Uses divide-and-conquer approach:
        - Recursively split the array of lists in half
        - Merge the results of left and right halves
        - Base case: single list or empty

        Time Complexity: O(n*k*log(k)) where n is average list length
        Space Complexity: O(log(k)) for recursion stack
        """
        if not lists or len(lists) == 0:
            return None

        return self._merge_lists(lists, 0, len(lists) - 1)

    def _merge_lists(
        self,
        lists: List[Optional[ListNode]],
        left: int,
        right: int
    ) -> Optional[ListNode]:
        """
        Recursively merge lists from left to right indices.
        """
        if left == right:
            return lists[left]

        if left > right:
            return None

        mid = (left + right) // 2
        left_merged = self._merge_lists(lists, left, mid)
        right_merged = self._merge_lists(lists, mid + 1, right)

        return self._merge_two_lists(left_merged, right_merged)

    def _merge_two_lists(
        self,
        list1: Optional[ListNode],
        list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        """
        Merge two sorted linked lists into one sorted list.
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


