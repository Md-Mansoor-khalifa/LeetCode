from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        Remove all occurrences of `val` in-place and return the new length k.

        Uses two-pointer (overwrite) technique. Time O(n), space O(1).
        """
        write = 0
        for x in nums:
            if x != val:
                nums[write] = x
                write += 1
        return write


if __name__ == "__main__":
    sol = Solution()
    tests = [
        ([3, 2, 2, 3], 3, [2, 2]),
        ([0, 1, 2, 2, 3, 0, 4, 2], 2, [0, 1, 4, 0, 3]),
    ]

    for i, (nums, val, expected) in enumerate(tests, start=1):
        arr = nums.copy()
        k = sol.removeElement(arr, val)
        out = arr[:k]
        # For judge compatibility, order of out doesn't matter; compare as multisets
        out_sorted = sorted(out)
        expected_sorted = sorted(expected)
        print(f"Test {i}: nums={nums}, val={val}")
        print(f"k: {k}, out: {out}")
        print(f"Match: {k == len(expected) and out_sorted == expected_sorted}")
        print()
