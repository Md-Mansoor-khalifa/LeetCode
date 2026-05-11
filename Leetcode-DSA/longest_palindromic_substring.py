class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        Find the longest palindromic substring using expand around center approach.
        
        Time Complexity: O(n²) - n centers * O(n) for expanding around each center
        Space Complexity: O(1) - only storing the result
        
        Args:
            s: Input string (1 <= s.length <= 1000)
        
        Returns:
            The longest palindromic substring
        """
        def expand_around_center(left: int, right: int) -> tuple:
            """
            Expand around center and return (start_index, length) of palindrome.
            
            Args:
                left: Left center index
                right: Right center index
            
            Returns:
                Tuple of (start_index, length) of palindrome
            """
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            
            # left and right went one step too far, so add 1 and subtract 1
            length = right - left - 1
            start = left + 1
            return start, length
        
        n = len(s)
        if n < 2:
            return s
        
        start = 0
        max_len = 1
        
        # Check all possible centers (both odd and even length palindromes)
        for i in range(n):
            # Odd length palindromes (single character center)
            s1, len1 = expand_around_center(i, i)
            
            # Even length palindromes (two character center)
            s2, len2 = expand_around_center(i, i + 1)
            
            # Update if we found a longer palindrome
            if len1 > max_len:
                start = s1
                max_len = len1
            
            if len2 > max_len:
                start = s2
                max_len = len2
        
        return s[start:start + max_len]


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    print(f"Input: s = \"babad\"")
    print(f"Output: {solution.longestPalindrome('babad')}")
    print(f"Expected: \"bab\" or \"aba\"\n")
    
    # Test case 2
    print(f"Input: s = \"cbbd\"")
    print(f"Output: {solution.longestPalindrome('cbbd')}")
    print(f"Expected: \"bb\"\n")
    
    # Test case 3 - Single character
    print(f"Input: s = \"a\"")
    print(f"Output: {solution.longestPalindrome('a')}")
    print(f"Expected: \"a\"\n")
    
    # Test case 4 - Entire string is palindrome
    print(f"Input: s = \"racecar\"")
    print(f"Output: {solution.longestPalindrome('racecar')}")
    print(f"Expected: \"racecar\"\n")
    
    # Test case 5 - No palindrome longer than 1
    print(f"Input: s = \"abc\"")
    print(f"Output: {solution.longestPalindrome('abc')}")
    print(f"Expected: \"a\" or \"b\" or \"c\"\n")
