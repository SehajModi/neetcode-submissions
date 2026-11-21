class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}                          # number -> index
        for i in range(len(nums)):
            partner = target - nums[i]
            if partner in seen:
                return [nums.index(partner), i]
            seen[nums[i]] = i