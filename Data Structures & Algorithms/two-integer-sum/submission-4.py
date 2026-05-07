class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # nums [1, 2, 3, 4]
        # target = 5 
        # 1 --> [2, 3, 4]
        # dict[1] = 0, complement = 4 (not in dict)
        # dict[2] = 1, complement = 3 (not in dict)
        # dict[3] = 2, complement = 2 (in dict) -> return [dict[2], i]

        seen = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in seen:
                return [seen[complement], i]
            seen[nums[i]] = i