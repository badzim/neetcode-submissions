class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False
        # Je dois construire un disctionnaire avec nombre de fois que j'ai vu un element
        result = {}
        for char in s:
            result[char] = result.get(char, 0) + 1
        for char in t:
            result[char] = result.get(char, 0) - 1
        # si la clé de l'un n'est pas dans l'autre c'est False
        return all(v == 0 for v in result.values())
        return True