class Solution:
    def minimumOperations(self, nums: list[int]) -> int:
        nums.sort()
        operations = 1 if nums[0] != 0 else 0
        
        for i in range(1,len(nums)):
            if nums[i] != 0 and nums[i] != nums[i-1]:
                operations += 1
                
        return operations
        