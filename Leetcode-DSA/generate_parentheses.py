from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        Generate all combinations of well-formed parentheses for n pairs.

        Uses backtracking to explore valid combinations:
        - Add opening parenthesis if we haven't used all n opening parentheses
        - Add closing parenthesis if we have more closing than opening remaining
        """
        result: List[str] = []

        def backtrack(
            current: str,
            open_count: int,
            close_count: int
        ) -> None:
            """
            Recursively build valid parentheses combinations.

            Args:
                current: Current combination being built
                open_count: Number of opening parentheses used so far
                close_count: Number of closing parentheses used so far
            """
            # Base case: we've placed all n pairs
            if open_count == n and close_count == n:
                result.append(current)
                return

            # Add opening parenthesis if we can
            if open_count < n:
                backtrack(current + "(", open_count + 1, close_count)

            # Add closing parenthesis if it's valid
            # (we need more closing than opening remaining, OR we have unmatched opening)
            if close_count < open_count:
                backtrack(current + ")", open_count, close_count + 1)

        backtrack("", 0, 0)
        return result


if __name__ == "__main__":
    sol = Solution()
    tests = [
        (1, ["()"]),
        (3, ["((()))", "(()())", "(())()", "()(())", "()()()"]),
        (2, ["(())", "()()"]),
    ]

    for i, (n, expected) in enumerate(tests, start=1):
        result = sol.generateParenthesis(n)
        result_sorted = sorted(result)
        expected_sorted = sorted(expected)
        print(f"Test {i}: n={n}")
        print(f"Output: {result_sorted}")
        print(f"Expected: {expected_sorted}")
        print(f"Match: {result_sorted == expected_sorted}")
        print()
