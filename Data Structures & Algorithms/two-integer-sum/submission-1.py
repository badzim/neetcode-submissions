class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        # i need indices i and j such that nums[i] + nums[j] == target and i != j
        # for example i = 1 and j = 2 ... i != j and nums[1] + nums[2] == 5