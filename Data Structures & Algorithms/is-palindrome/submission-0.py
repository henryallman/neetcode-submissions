class Solution:
    def isPalindrome(self, s: str) -> bool:
        word = ""
        for char in s:
            if char.isalpha():
                word += char.lower()
            elif char.isdigit():
                word += char
        return word == word[::-1]