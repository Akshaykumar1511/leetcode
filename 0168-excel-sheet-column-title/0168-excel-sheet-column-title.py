class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = []
        
        while columnNumber > 0:
            # Adjust columnNumber to 0-indexed (1-based to 0-based conversion)
            columnNumber -= 1
            
            # Find the remainder to get the current character and convert to ASCII
            remainder = columnNumber % 26
            result.append(chr(ord('A') + remainder))
            
            # Move to the next "digit" place value
            columnNumber //= 26
            
        # The characters are collected in reverse order (from least significant to most significant)
        return "".join(result[::-1])