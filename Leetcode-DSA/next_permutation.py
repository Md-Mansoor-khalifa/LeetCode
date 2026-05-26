from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Modify nums in-place to be the next lexicographically greater permutation.

        Algorithm:
        1. Find the largest index i such that nums[i] < nums[i+1]
        2. If no such index exists, reverse the entire array (already at last permutation)
        3. Find the largest index j > i such that nums[i] < nums[j]
        4. Swap nums[i] and nums[j]
        5. Reverse the suffix starting at nums[i+1]

        Time: O(n), Space: O(1)
        """
        i = len(nums) - 2
        
        # Step 1: Find the rightmost position i where nums[i] < nums[i+1]
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        
        # If no such i exists, we're at the last permutation; reverse to get first
        if i == -1:
            nums.reverse()
            return
        
        # Step 2: Find the rightmost position j > i where nums[j] > nums[i]
        j = len(nums) - 1
        while j > i and nums[j] <= nums[i]:
            j -= 1
        
        # Step 3: Swap nums[i] and nums[j]
        nums[i], nums[j] = nums[j], nums[i]
        
        # Step 4: Reverse the suffix starting at nums[i+1]
        nums[i + 1:] = reversed(nums[i + 1:])


if __name__ == "__main__":
    sol = Solution()
    tests = [
        ([1, 2, 3], [1, 3, 2]),
        ([3, 2, 1], [1, 2, 3]),
        ([1, 1, 5], [1, 5, 1]),
        ([1], [1]),
        ([1, 3, 2], [2, 1, 3]),
        ([2, 3, 1], [3, 1, 2]),
    ]

    for i, (nums, expected) in enumerate(tests, start=1):
        arr = nums.copy()
        sol.nextPermutation(arr)
        print(f"Test {i}: input={nums}")
        print(f"Output: {arr}, Expected: {expected}")
        print(f"Pass: {arr == expected}")
        print()
