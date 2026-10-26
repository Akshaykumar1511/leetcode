class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result = 0
        for char in columnTitle:
            # Shift previous result left in base 26 and add current value
            result = result * 26 + (ord(char) - ord('A') + 1)
        return result