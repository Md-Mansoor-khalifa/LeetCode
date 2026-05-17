from typing import Dict


class Solution:
    def isValid(self, s: str) -> bool:
        """
        Determine whether the input string of brackets is valid.

        Uses a stack to match each closing bracket with the most recent open bracket.
        """
        matching: Dict[str, str] = {
            ")": "(",
            "]": "[",
            "}": "{",
        }
        stack: list[str] = []

        for char in s:
            if char in matching.values():
                stack.append(char)
            elif char in matching:
                if not stack or stack[-1] != matching[char]:
                    return False
                stack.pop()
            else:
                # Since constraints guarantee only bracket characters, this is defensive.
                return False

        return not stack


if __name__ == "__main__":
    sol = Solution()
    tests = [
        ("()", True),
        ("()[]{}", True),
        ("(]", False),
        ("([])", True),
        ("([)]", False),
    ]

    for i, (s, expected) in enumerate(tests, start=1):
        result = sol.isValid(s)
        print(f"Test {i}: s='{s}'")
        print(f"Output: {result}")
        print(f"Expected: {expected}")
        print()