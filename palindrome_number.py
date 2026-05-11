class Solution:
    def isPalindrome(self, x: int) -> bool:
        """Return True if x is a palindrome integer without converting it to a string."""
        # Negative numbers are not palindromes due to the '-' sign.
        if x < 0:
            return False

        # Numbers ending with 0 are only palindromes if the number is 0.
        if x != 0 and x % 10 == 0:
            return False

        reversed_half = 0
        while x > reversed_half:
            reversed_half = reversed_half * 10 + x % 10
            x //= 10

        # For odd-length numbers, discard the middle digit before comparison.
        return x == reversed_half or x == reversed_half // 10


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        (121, True),
        (-121, False),
        (10, False),
        (0, True),
        (1221, True),
        (123, False),
        (1001, True),
    ]

    for x, expected in test_cases:
        result = solution.isPalindrome(x)
        print(f"Input: {x}\nOutput: {result}\nExpected: {expected}\n")
