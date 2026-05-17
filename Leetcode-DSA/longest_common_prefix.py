from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Edge case: empty list
        if not strs:
            return ""
        
        # Find the minimum length among all strings
        min_len = min(len(s) for s in strs)
        
        # Vertical scanning: compare characters at the same position across all strings
        for i in range(min_len):
            char = strs[0][i]
            # Check if all strings have the same character at position i
            for j in range(1, len(strs)):
                if strs[j][i] != char:
                    # Mismatch found, return prefix up to this point
                    return strs[0][:i]
        
        # If we've checked all positions up to min_len, return that prefix
        return strs[0][:min_len]
