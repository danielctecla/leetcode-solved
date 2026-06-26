class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [1] * len(nums)
        
        curr = 1
        for i in range(1, n):
            ans[i] = curr * nums[i - 1]
            curr *= nums[i - 1]
        
        curr = 1
        for i in range(n - 2, -1, -1):
            ans[i] *= curr * nums[i + 1]
            curr *= nums[i + 1]
            
        return ans


        
        