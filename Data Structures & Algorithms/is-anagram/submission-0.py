class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = [0] * 26
        count2 = [0] * 26
        
        for char in s:
            count[ord(char) - ord('a')] += 1
        for char in t:
            count2[ord(char) - ord('a')] += 1
        
        return True if count == count2 else False