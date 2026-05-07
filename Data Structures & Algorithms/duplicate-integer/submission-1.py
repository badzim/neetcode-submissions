class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        deja_vu : set = set() # O(1)
        for number in nums: # O(n)
            if number in deja_vu: # ~O(1) car hash map
                return True
            deja_vu.add(number)
        return False