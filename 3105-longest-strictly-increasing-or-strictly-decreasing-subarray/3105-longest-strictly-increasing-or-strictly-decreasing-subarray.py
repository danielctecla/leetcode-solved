class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        ans = 1

        current = 1

        for i in range(1,len(nums)):
            if nums[i] <= nums[i - 1]:
                current = 1
                continue
            
            current += 1
            ans = max(current, ans)
        
        current = 1
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] <= nums[i + 1]:
                current = 1
                continue 

            current += 1
            ans = max(current, ans)
            
        return ans