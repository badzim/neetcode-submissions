class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False
        result = {}
        for char in s:
            result[char] = result.get(char, 0) + 1
        for char in t:
            result[char] = result.get(char, 0) - 1
        return all(v == 0 for v in result.values())