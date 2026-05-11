from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Add two numbers represented as linked lists in reverse order.
        
        The digits are stored in reverse order, so the ones place is at the head.
        For example: [2,4,3] represents 342.
        
        Args:
            l1: First linked list (digits in reverse order)
            l2: Second linked list (digits in reverse order)
            
        Returns:
            A new linked list representing the sum (digits in reverse order)
            
        Time Complexity: O(max(len(l1), len(l2)))
        Space Complexity: O(max(len(l1), len(l2))) for the result list
        """
        # Create a dummy node to simplify the logic
        dummy_head = ListNode(0)
        current = dummy_head
        carry = 0
        
        # Traverse both lists until we've processed all nodes and there's no carry
        while l1 or l2 or carry:
            # Get values from current nodes (0 if node is None)
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # Calculate sum and carry
            total = val1 + val2 + carry
            carry = total // 10
            digit = total % 10
            
            # Create new node with the digit and append to result
            current.next = ListNode(digit)
            current = current.next
            
            # Move to next nodes in both lists
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        return dummy_head.next


# Test cases
if __name__ == "__main__":
    # Helper function to create linked list from array
    def create_linked_list(arr):
        if not arr:
            return None
        head = ListNode(arr[0])
        current = head
        for val in arr[1:]:
            current.next = ListNode(val)
            current = current.next
        return head
    
    # Helper function to convert linked list to array
    def linked_list_to_array(head):
        result = []
        current = head
        while current:
            result.append(current.val)
            current = current.next
        return result
    
    solution = Solution()
    
    # Test case 1: l1 = [2,4,3], l2 = [5,6,4]
    # 342 + 465 = 807 -> [7,0,8]
    l1 = create_linked_list([2, 4, 3])
    l2 = create_linked_list([5, 6, 4])
    result = solution.addTwoNumbers(l1, l2)
    print(f"Test 1: {linked_list_to_array(result)}")  # Expected: [7, 0, 8]
    
    # Test case 2: l1 = [0], l2 = [0]
    # 0 + 0 = 0 -> [0]
    l1 = create_linked_list([0])
    l2 = create_linked_list([0])
    result = solution.addTwoNumbers(l1, l2)
    print(f"Test 2: {linked_list_to_array(result)}")  # Expected: [0]
    
    # Test case 3: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
    # 9999999 + 9999 = 10009998 -> [8,9,9,9,0,0,0,1]
    l1 = create_linked_list([9, 9, 9, 9, 9, 9, 9])
    l2 = create_linked_list([9, 9, 9, 9])
    result = solution.addTwoNumbers(l1, l2)
    print(f"Test 3: {linked_list_to_array(result)}")  # Expected: [8, 9, 9, 9, 0, 0, 0, 1]
