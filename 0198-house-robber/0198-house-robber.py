class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)

        nums[1] = max(nums[0],nums[1])
        
        for idx in range(2,len(nums)):
            nums[idx] = max(nums[idx] + nums[idx - 2], nums[idx - 1])
        
        return nums[-1]

        