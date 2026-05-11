class Solution:
    def intToRoman(self, num: int) -> str:
        # Define the values and their corresponding Roman symbols in descending order
        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        symbols = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        
        result = []
        i = 0
        while num > 0:
            # Find the largest value that is less than or equal to num
            while values[i] > num:
                i += 1
            # Append the corresponding symbol
            result.append(symbols[i])
            # Subtract the value from num
            num -= values[i]
        
        # Join the list into a string
        return ''.join(result)