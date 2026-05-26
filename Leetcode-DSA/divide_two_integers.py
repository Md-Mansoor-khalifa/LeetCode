from __future__ import annotations


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        """
        Divide two integers without using multiplication, division, or mod.

        Uses bit shifting and subtraction to compute the quotient.
        Handles overflow within 32-bit signed integer range.
        """
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        if dividend == INT_MIN and divisor == -1:
            return INT_MAX

        negative = (dividend < 0) ^ (divisor < 0)
        a = abs(dividend)
        b = abs(divisor)

        result = 0
        while a >= b:
            shift = 0
            while a >= (b << shift):
                shift += 1
            shift -= 1
            result += 1 << shift
            a -= b << shift

        if negative:
            result = -result

        return max(INT_MIN, min(INT_MAX, result))


if __name__ == "__main__":
    sol = Solution()
    tests = [
        (10, 3, 3),
        (7, -3, -2),
        (0, 1, 0),
        (1, 1, 1),
        (-1, 1, -1),
        (-10, 3, -3),
        (INT_MAX := 2**31 - 1, 1, 2**31 - 1),
        (-2**31, -1, 2**31 - 1),
    ]

    for i, (dividend, divisor, expected) in enumerate(tests, start=1):
        out = sol.divide(dividend, divisor)
        print(f"Test {i}: dividend={dividend}, divisor={divisor}")
        print(f"Output: {out}, Expected: {expected}")
        print(f"Pass: {out == expected}")
        print()