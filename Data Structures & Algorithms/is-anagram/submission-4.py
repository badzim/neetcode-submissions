class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Je dois construire un disctionnaire avec nombre de fois que j'ai vu un element
        dict_s = self._construct_dict_occurence(s)
        dict_t = self._construct_dict_occurence(t)
        # si la clé de l'un n'est pas dans l'autre c'est False
        keys_s = dict_s.keys()
        keys_t = dict_t.keys() 
        if len(keys_s) != len(keys_t):
            return False
        for char in keys_s:
            if (char not in keys_t) or (dict_s[char] != dict_t[char]):
                return False
        return True
        

    def _construct_dict_occurence(self, s: str) -> dict[str, int]:
        result = {}
        deja_vu = set()
        for char in s:
            if char not in deja_vu:
                deja_vu.add(char)
                result[char] = 1
            else:
                result[char] += 1
        print(result)
        return result