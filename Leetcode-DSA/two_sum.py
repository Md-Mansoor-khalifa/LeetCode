class TwoSum:
    """
    Find two numbers that add up to the target
    
    Approach: HashMap (Hash Table)
    Time Complexity: O(n)
    Space Complexity: O(n)
    
    Algorithm:
    1. Iterate through the array once
    2. For each number, check if (target - number) exists in the HashMap
    3. If it exists, we found our pair
    4. If not, add the current number and its index to the HashMap
    5. Return the indices of the two numbers
    """
    
    def twoSum(self, nums, target):
        """
        Find indices of two numbers that add up to target
        
        Args:
            nums: List of integers
            target: Target sum
            
        Returns:
            List of two indices
        """
        # Dictionary to store value -> index mapping
        num_map = {}
        
        for i, num in enumerate(nums):
            complement = target - num
            
            # Check if the complement exists in the dictionary
            if complement in num_map:
                # Return indices (complement's index, current index)
                return [num_map[complement], i]
            
            # Store the current number and its index
            num_map[num] = i
        
        # No solution found (though problem guarantees one exists)
        return []
    
    def twoSumBruteForce(self, nums, target):
        """
        Alternative Brute Force Approach (for reference)
        Time Complexity: O(n^2)
        Space Complexity: O(1)
        """
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []


def main():
    """Test cases"""
    solution = TwoSum()
    
    # Test Case 1
    nums1 = [2, 7, 11, 15]
    target1 = 9
    result1 = solution.twoSum(nums1, target1)
    print("Test 1 - Input: nums = [2,7,11,15], target = 9")
    print(f"Output: {result1}")
    print("Expected: [0,1]\n")
    
    # Test Case 2
    nums2 = [3, 2, 4]
    target2 = 6
    result2 = solution.twoSum(nums2, target2)
    print("Test 2 - Input: nums = [3,2,4], target = 6")
    print(f"Output: {result2}")
    print("Expected: [1,2]\n")
    
    # Test Case 3
    nums3 = [3, 3]
    target3 = 6
    result3 = solution.twoSum(nums3, target3)
    print("Test 3 - Input: nums = [3,3], target = 6")
    print(f"Output: {result3}")
    print("Expected: [0,1]")


if __name__ == "__main__":
    main()
