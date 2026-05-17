from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Sort the array to enable two-pointer approach and handle duplicates
        nums.sort()
        result = []
        n = len(nums)
        
        # Iterate through each element as the first number in the triplet
        for i in range(n - 2):
            # Optimization: if current number is positive, no triplet can sum to 0
            if nums[i] > 0:
                break
            
            # Skip duplicate values for the first element
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            # Use two pointers to find pairs that sum to -nums[i]
            left = i + 1
            right = n - 1
            target = -nums[i]
            
            while left < right:
                current_sum = nums[left] + nums[right]
                
                if current_sum == target:
                    result.append([nums[i], nums[left], nums[right]])
                    
                    # Skip duplicates for the second element
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    # Skip duplicates for the third element
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    left += 1
                    right -= 1
                elif current_sum < target:
                    # Need larger sum, move left pointer right
                    left += 1
                else:
                    # Need smaller sum, move right pointer left
                    right -= 1
        
        return result
