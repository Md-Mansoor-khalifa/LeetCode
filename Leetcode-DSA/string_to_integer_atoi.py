class Solution:
    def myAtoi(self, s: str) -> int:
        """Convert a string to a 32-bit signed integer.

        Steps:
        1. Ignore leading whitespace.
        2. Detect optional sign (+ or -).
        3. Read digits until a non-digit character is reached.
        4. Ignore leading zeros during conversion.
        5. Clamp result to the 32-bit signed range.
        """
        s = s.lstrip()
        if not s:
            return 0

        sign = 1
        index = 0
        if s[0] in {"-", "+"}:
            if s[0] == "-":
                sign = -1
            index += 1

        total = 0
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        while index < len(s) and s[index].isdigit():
            digit = ord(s[index]) - ord("0")
            # Check overflow before adding the digit
            if total > (INT_MAX - digit) // 10:
                return INT_MAX if sign == 1 else INT_MIN
            total = total * 10 + digit
            index += 1

        return sign * total


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        ("42", 42),
        ("   -042", -42),
        ("1337c0d3", 1337),
        ("0-1", 0),
        ("words and 987", 0),
        ("-91283472332", -2147483648),
        ("91283472332", 2147483647),
        ("   +0 123", 0),
        ("", 0),
        ("+", 0),
        ("-", 0),
        ("  0000000000012345678", 12345678),
    ]

    for s, expected in test_cases:
        result = solution.myAtoi(s)
        print(f"Input: {s!r}\nOutput: {result}\nExpected: {expected}\n")
