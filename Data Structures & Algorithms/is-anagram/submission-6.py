class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False
        # Je dois construire un disctionnaire avec nombre de fois que j'ai vu un element
        dict_s = self._construct_dict_occurence(s)
        dict_t = self._construct_dict_occurence(t)
        # si la clé de l'un n'est pas dans l'autre c'est False
        keys_s = dict_s.keys()
        keys_t = dict_t.keys() 
        for char in keys_s:
            if (char not in keys_t) or (dict_s[char] != dict_t[char]):
                return False
        return True
        

    def _construct_dict_occurence(self, s: str) -> dict[str, int]:
        result = {}
        for char in s:
            result[char] = result.get(char, 0) + 1
        return result