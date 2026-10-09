class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set("aeiouAEIOU")
        # Extract vowels in order
        found_vowels = [char for char in s if char in vowels]
        
        res = []
        for char in s:
            if char in vowels:
                res.append(found_vowels.pop())  # Pop from the end to reverse order
            else:
                res.append(char)
                
        return "".join(res)
