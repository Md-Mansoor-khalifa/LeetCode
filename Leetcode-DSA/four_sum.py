from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        """
        Find all unique quadruplets that sum to target.
        Uses recursive approach to generalize to k-sum problem.
        
        Time Complexity: O(n^3)
        Space Complexity: O(1) excluding output
        """
        nums.sort()
        result = []
        self.k_sum(nums, target, 4, 0, [], result)
        return result
    
    def k_sum(
        self,
        nums: List[int],
        target: int,
        k: int,
        start: int,
        current: List[int],
        result: List[List[int]]
    ) -> None:
        """
        Recursive helper function to find all k-sum combinations.
        
        Args:
            nums: Sorted array of integers
            target: Target sum
            k: Number of elements to find
            start: Starting index
            current: Current combination being built
            result: List to store all valid quadruplets
        """
        # Base case: when k == 2, use two-pointer technique
        if k == 2:
            self.two_sum(nums, target, start, current, result)
            return
        
        # Recursive case: fix one element and reduce to (k-1)sum
        for i in range(start, len(nums)):
            # Skip duplicates
            if i > start and nums[i] == nums[i - 1]:
                continue
            
            n = len(nums)
            # Early termination: if smallest possible sum is too large
            # min_sum = nums[i] + sum of k-1 smallest elements after i
            if i + k <= n:
                min_sum = nums[i] + sum(nums[i + 1:i + k])
                if min_sum > target:
                    break
            
            # Early termination: if largest possible sum is too small
            # max_sum = nums[i] + sum of k-1 largest elements
            max_sum = nums[i] + sum(nums[n - (k - 1):])
            if max_sum < target:
                continue
            
            # Recurse with reduced problem
            self.k_sum(
                nums,
                target - nums[i],
                k - 1,
                i + 1,
                current + [nums[i]],
                result
            )
    
    def two_sum(
        self,
        nums: List[int],
        target: int,
        start: int,
        current: List[int],
        result: List[List[int]]
    ) -> None:
        """
        Base case: find all pairs that sum to target using two pointers.
        
        Args:
            nums: Sorted array of integers
            target: Target sum
            start: Starting index
            current: Current combination (already has 3 elements)
            result: List to store all valid quadruplets
        """
        left = start
        right = len(nums) - 1
        
        while left < right:
            current_sum = nums[left] + nums[right]
            
            if current_sum == target:
                result.append(current + [nums[left], nums[right]])
                
                # Skip duplicates
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                
                left += 1
                right -= 1
            elif current_sum < target:
                left += 1
            else:
                right -= 1


if __name__ == "__main__":
    sol = Solution()
    
    # Test case 1
    nums1 = [1, 0, -1, 0, -2, 2]
    target1 = 0
    print("Test 1:")
    print(f"Input: nums = {nums1}, target = {target1}")
    print(f"Output: {sol.fourSum(nums1, target1)}")
    print(f"Expected: [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]")
    print()
    
    # Test case 2
    nums2 = [2, 2, 2, 2, 2]
    target2 = 8
    print("Test 2:")
    print(f"Input: nums = {nums2}, target = {target2}")
    print(f"Output: {sol.fourSum(nums2, target2)}")
    print(f"Expected: [[2, 2, 2, 2]]")
    print()
    
    # Test case 3: edge case with negative numbers
    nums3 = [-1000000000, 1000000000, 1, 0, 0]
    target3 = 0
    print("Test 3:")
    print(f"Input: nums = {nums3}, target = {target3}")
    print(f"Output: {sol.fourSum(nums3, target3)}")
    print(f"Expected: [[-1000000000, 0, 0, 1000000000]]")
