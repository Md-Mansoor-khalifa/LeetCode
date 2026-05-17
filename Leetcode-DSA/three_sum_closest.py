from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # Sort the array to enable two-pointer approach
        nums.sort()
        n = len(nums)
        result = nums[0] + nums[1] + nums[2]
        
        # Iterate through each element as the first number in the triplet
        for i in range(n - 2):
            n_i = nums[i]
            
            # Skip duplicate values for the first element
            if i > 0 and n_i == nums[i - 1]:
                continue
            
            # Early boundary checks to prune search space
            min_sum = nums[i] + nums[i + 1] + nums[i + 2]
            max_sum = nums[i] + nums[n - 2] + nums[n - 1]
            
            # If minimum possible sum is already larger than target, 
            # it's the closest we can get, so break
            if min_sum > target:
                if abs(min_sum - target) < abs(result - target):
                    result = min_sum
                break
            
            # If maximum possible sum is smaller than target,
            # update result and skip to next i
            if max_sum < target:
                result = max_sum
                continue
            
            # Use two pointers to find the pair closest to target - nums[i]
            left = i + 1
            right = n - 1
            
            while left < right:
                n_j = nums[left]
                n_k = nums[right]
                current_sum = n_i + n_j + n_k
                
                # Update result if this sum is closer to target
                if abs(current_sum - target) < abs(result - target):
                    result = current_sum
                
                # If we found exact match, return immediately (optimal)
                if current_sum == target:
                    return current_sum
                elif current_sum < target:
                    # Need larger sum, move left pointer right
                    left += 1
                else:
                    # Need smaller sum, move right pointer left
                    right -= 1
        
        return result
