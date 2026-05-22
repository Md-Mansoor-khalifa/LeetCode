from typing import List


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        """
        Return the index of the first occurrence of needle in haystack or -1.

        Implements Knuth-Morris-Pratt (KMP) algorithm for O(n + m) time.
        """
        if needle == "":
            return 0

        # Build longest proper prefix which is also suffix (lps) array for needle
        lps = self._build_lps(needle)

        i = 0  # index for haystack
        j = 0  # index for needle
        n = len(haystack)
        m = len(needle)

        while i < n:
            if haystack[i] == needle[j]:
                i += 1
                j += 1
                if j == m:
                    return i - j
            else:
                if j != 0:
                    j = lps[j - 1]
                else:
                    i += 1

        return -1

    def _build_lps(self, pattern: str) -> List[int]:
        m = len(pattern)
        lps = [0] * m
        length = 0  # length of previous longest prefix suffix
        i = 1
        while i < m:
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1
        return lps


if __name__ == "__main__":
    sol = Solution()
    tests = [
        ("sadbutsad", "sad", 0),
        ("leetcode", "leeto", -1),
        ("aaaaa", "bba", -1),
        ("hello", "ll", 2),
        ("", "", 0),
        ("a", "a", 0),
    ]

    for i, (haystack, needle, expected) in enumerate(tests, start=1):
        out = sol.strStr(haystack, needle)
        print(f"Test {i}: haystack='{haystack}', needle='{needle}' -> {out} (expected {expected})")
        print(f"Pass: {out == expected}")
        print()
