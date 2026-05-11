from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        Find the median of two sorted arrays using binary search.
        
        Time Complexity: O(log(min(m, n))) where m and n are lengths of nums1 and nums2
        Space Complexity: O(1)
        
        Approach:
        - Use binary search on the smaller array to find the correct partition
        - A valid partition divides both arrays such that all elements on the left
          are <= all elements on the right
        - Calculate median from the partition boundaries
        """
        # Ensure nums1 is the smaller array for optimization
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        m, n = len(nums1), len(nums2)
        low, high = 0, m
        
        while low <= high:
            partition1 = (low + high) // 2
            partition2 = (m + n + 1) // 2 - partition1
            
            # Handle edge cases for partition boundaries
            left1 = float('-inf') if partition1 == 0 else nums1[partition1 - 1]
            left2 = float('-inf') if partition2 == 0 else nums2[partition2 - 1]
            right1 = float('inf') if partition1 == m else nums1[partition1]
            right2 = float('inf') if partition2 == n else nums2[partition2]
            
            # Check if we found the correct partition
            if left1 <= right2 and left2 <= right1:
                # If total length is even, return average of two middle elements
                if (m + n) % 2 == 0:
                    return (max(left1, left2) + min(right1, right2)) / 2.0
                # If total length is odd, return the larger of the left partition
                else:
                    return float(max(left1, left2))
            # Move partition1 to the right if left1 > right2
            elif left1 > right2:
                high = partition1 - 1
            # Move partition1 to the left if left2 > right1
            else:
                low = partition1 + 1
        
        return -1.0  # Should never reach here with valid input


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Example 1: merged array = [1,2,3], median = 2
    result1 = solution.findMedianSortedArrays([1, 3], [2])
    print(f"Example 1: {result1}")  # Expected: 2.0
    assert result1 == 2.0, f"Expected 2.0, got {result1}"
    
    # Example 2: merged array = [1,2,3,4], median = (2+3)/2 = 2.5
    result2 = solution.findMedianSortedArrays([1, 2], [3, 4])
    print(f"Example 2: {result2}")  # Expected: 2.5
    assert result2 == 2.5, f"Expected 2.5, got {result2}"
    
    # Edge case: one empty array
    result3 = solution.findMedianSortedArrays([], [1])
    print(f"Edge case 1 (empty array): {result3}")  # Expected: 1.0
    assert result3 == 1.0, f"Expected 1.0, got {result3}"
    
    # Edge case: single element each
    result4 = solution.findMedianSortedArrays([1], [2])
    print(f"Edge case 2 (single elements): {result4}")  # Expected: 1.5
    assert result4 == 1.5, f"Expected 1.5, got {result4}"
    
    # Edge case: negative numbers
    result5 = solution.findMedianSortedArrays([-2, 0], [1, 2])
    print(f"Edge case 3 (negative numbers): {result5}")  # Expected: 0.5
    assert result5 == 0.5, f"Expected 0.5, got {result5}"
    
    print("\nAll tests passed!")
