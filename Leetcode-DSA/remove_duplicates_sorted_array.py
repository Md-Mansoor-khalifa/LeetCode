from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        Remove duplicates in-place from a sorted list and return the number
        of unique elements (k). The first k elements of nums will hold the
        unique values in order.

        Uses two-pointer technique: `write_index` tracks where to write the
        next unique value.
        Time: O(n), Space: O(1)
        """
        if not nums:
            return 0

        write_index = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[write_index] = nums[i]
                write_index += 1

        return write_index


if __name__ == "__main__":
    sol = Solution()
    tests = [
        ([1, 1, 2], [1, 2]),
        ([0, 0, 1, 1, 1, 2, 2, 3, 3, 4], [0, 1, 2, 3, 4]),
    ]

    for nums, expected in tests:
        arr = nums.copy()
        k = sol.removeDuplicates(arr)
        print(f"Input: {nums}")
        print(f"k: {k}, nums[:k]: {arr[:k]}, expected: {expected}")
        print(f"Pass: {k == len(expected) and arr[:k] == expected}")
        print()
