class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False
        # Je dois construire un disctionnaire avec nombre de fois que j'ai vu un element
        dict_s = self._construct_dict_occurence(s)
        dict_t = self._construct_dict_occurence(t)
        # si la clé de l'un n'est pas dans l'autre c'est False
        return dict_s == dict_t
        

    def _construct_dict_occurence(self, s: str) -> dict[str, int]:
        result = {}
        for char in s:
            result[char] = result.get(char, 0) + 1
        return result