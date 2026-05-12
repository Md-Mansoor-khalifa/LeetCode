class Solution:
    def romanToInt(self, s: str) -> int:
        # Dictionary mapping Roman symbols to their integer values
        roman_values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        total = 0
        i = 0
        
        while i < len(s):
            # If current symbol's value is less than next symbol's value,
            # it's a subtractive case (e.g., IV, IX, XL, etc.)
            if i + 1 < len(s) and roman_values[s[i]] < roman_values[s[i + 1]]:
                total += roman_values[s[i + 1]] - roman_values[s[i]]
                i += 2  # Skip next character since we've processed it
            else:
                # Otherwise, just add the current symbol's value
                total += roman_values[s[i]]
                i += 1
        
        return total
