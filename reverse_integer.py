class Solution:
    def reverse(self, x: int) -> int:
        """
        Reverse the digits of a signed 32-bit integer.
        
        Time Complexity: O(log x) - number of digits in x
        Space Complexity: O(1) - only using a few variables
        
        Args:
            x: Signed 32-bit integer (-2^31 <= x <= 2^31 - 1)
        
        Returns:
            Reversed integer, or 0 if overflow occurs
        
        Note: The 32-bit integer range is [-2147483648, 2147483647]
        """
        # Define 32-bit integer range
        INT_MIN = -2**31  # -2147483648
        INT_MAX = 2**31 - 1  # 2147483647
        
        # Store the sign and work with absolute value
        sign = -1 if x < 0 else 1
        x = abs(x)
        
        # Reverse the digits
        result = 0
        while x > 0:
            digit = x % 10
            
            # Check for overflow BEFORE updating result
            # This avoids storing 64-bit integers
            # If result > INT_MAX // 10, then result * 10 will overflow
            # If result == INT_MAX // 10 and digit > 7, it will also overflow
            if result > INT_MAX // 10 or (result == INT_MAX // 10 and digit > 7):
                return 0
            
            result = result * 10 + digit
            x //= 10
        
        # Apply the sign and check final bounds
        result = sign * result
        
        return result if INT_MIN <= result <= INT_MAX else 0


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1: Positive number
    print("Test Case 1:")
    x1 = 123
    print(f"Input: x = {x1}")
    print(f"Output: {solution.reverse(x1)}")
    print(f"Expected: 321\n")
    
    # Test case 2: Negative number
    print("Test Case 2:")
    x2 = -123
    print(f"Input: x = {x2}")
    print(f"Output: {solution.reverse(x2)}")
    print(f"Expected: -321\n")
    
    # Test case 3: Number ending with zero
    print("Test Case 3:")
    x3 = 120
    print(f"Input: x = {x3}")
    print(f"Output: {solution.reverse(x3)}")
    print(f"Expected: 21\n")
    
    # Test case 4: Overflow - would exceed INT_MAX
    print("Test Case 4:")
    x4 = 1534236469
    print(f"Input: x = {x4}")
    print(f"Output: {solution.reverse(x4)}")
    print(f"Expected: 0 (overflow)\n")
    
    # Test case 5: Single digit
    print("Test Case 5:")
    x5 = 0
    print(f"Input: x = {x5}")
    print(f"Output: {solution.reverse(x5)}")
    print(f"Expected: 0\n")
    
    # Test case 6: Large negative number
    print("Test Case 6:")
    x6 = -2147483648
    print(f"Input: x = {x6}")
    print(f"Output: {solution.reverse(x6)}")
    print(f"Expected: 0 (overflow)\n")
