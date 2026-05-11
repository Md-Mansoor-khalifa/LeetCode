class Solution:
    def convert(self, s: str, numRows: int) -> str:
        """
        Convert a string into zigzag pattern and read line by line.
        
        Time Complexity: O(n) - single pass through the string
        Space Complexity: O(n) - storing characters in rows
        
        Args:
            s: Input string (1 <= s.length <= 1000)
            numRows: Number of rows in zigzag pattern (1 <= numRows <= 1000)
        
        Returns:
            String read line by line from zigzag pattern
        
        Example:
            Input: s = "PAYPALISHIRING", numRows = 3
            Output: "PAHNAPLSIIGYIR"
            
            Pattern:
            P   A   H   N
            A P L S I I G
            Y   I   R
        """
        # Edge case: single row
        if numRows == 1:
            return s
        
        # Create a list to store characters for each row
        rows = [[] for _ in range(numRows)]
        row = 0
        direction = 1  # 1 for moving down, -1 for moving up
        
        # Place each character in its corresponding row
        for char in s:
            rows[row].append(char)
            
            # Change direction at the boundaries
            if row == 0:
                direction = 1  # Start going down
            elif row == numRows - 1:
                direction = -1  # Start going up
            
            # Move to next row
            row += direction
        
        # Concatenate all rows to get the result
        result = ""
        for row_chars in rows:
            result += "".join(row_chars)
        
        return result


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    print("Test Case 1:")
    s1 = "PAYPALISHIRING"
    numRows1 = 3
    print(f"Input: s = \"{s1}\", numRows = {numRows1}")
    print(f"Output: {solution.convert(s1, numRows1)}")
    print(f"Expected: \"PAHNAPLSIIGYIR\"\n")
    
    # Test case 2
    print("Test Case 2:")
    s2 = "PAYPALISHIRING"
    numRows2 = 4
    print(f"Input: s = \"{s2}\", numRows = {numRows2}")
    print(f"Output: {solution.convert(s2, numRows2)}")
    print(f"Expected: \"PINALSIGYAHRPI\"\n")
    
    # Test case 3 - Single row
    print("Test Case 3:")
    s3 = "A"
    numRows3 = 1
    print(f"Input: s = \"{s3}\", numRows = {numRows3}")
    print(f"Output: {solution.convert(s3, numRows3)}")
    print(f"Expected: \"A\"\n")
    
    # Test case 4 - Two rows
    print("Test Case 4:")
    s4 = "ABCDEFG"
    numRows4 = 2
    print(f"Input: s = \"{s4}\", numRows = {numRows4}")
    print(f"Output: {solution.convert(s4, numRows4)}")
    print(f"Expected: \"ACEGBDF\"\n")
    
    # Test case 5 - Many rows (more rows than characters)
    print("Test Case 5:")
    s5 = "ABC"
    numRows5 = 5
    print(f"Input: s = \"{s5}\", numRows = {numRows5}")
    print(f"Output: {solution.convert(s5, numRows5)}")
    print(f"Expected: \"ABC\"\n")
