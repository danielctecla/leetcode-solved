class Solution:
    
    @staticmethod
    def getMaxRob(nums: List[int]) -> int:
        ans = nums[0]
        
        for i in range(1,len(nums)):
            current = nums[i]
            for j in range(2,4):
                if i - j >= 0:
                    nums[i] = max(nums[i], current + nums[i - j])
                    
            ans = max(nums[i], ans)
        return ans  

    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
            
        return max(
                self.getMaxRob(nums[0:n-1]),
                self.getMaxRob(nums[1:n])
            )