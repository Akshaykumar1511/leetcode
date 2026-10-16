class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        # 1. Convert the 2D list into a dictionary for O(1) string lookups
        know_dict = {k: v for k, v in knowledge}
        
        res = []
        temp = []
        in_bracket = False
        
        for char in s:
            if char == "(":
                in_bracket = True
            elif char == ")":
                # 2. Look up the key. .get() returns "?" if the key doesn't exist.
                key = "".join(temp)
                res.append(know_dict.get(key, "?"))
                
                # Reset for the next bracket pair
                temp = []
                in_bracket = False
            elif in_bracket:
                temp.append(char)
            else:
                res.append(char)
                
        # 3. Join the array into a single string (faster than res += char)
        return "".join(res)